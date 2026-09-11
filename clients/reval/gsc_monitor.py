#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REVAL - Google Search Console monitor (read-only).

Usage:
    python gsc_monitor.py                    # list GSC sites and default report
    python gsc_monitor.py --inspect          # URL inspection for reval-sa.com pages
    python gsc_monitor.py --performance      # last 28 days impressions/clicks
    python gsc_monitor.py --all              # full report
"""
import argparse
import json
import os
import sys

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
API = "https://searchconsole.googleapis.com/webmasters/v3"
API_V1 = "https://searchconsole.googleapis.com/v1"
KEY = r"D:\Projects\Reval-Operations\seo\athman-arbaa-d0d6ae066f38.json"
SITE = None  # auto-detected

PREFIX = "https://reval-sa.com"
PAGES = [
    "/", "/about-us/", "/why-reval/", "/services/", "/industries/",
    "/hse-sustainability/", "/contact-us/", "/join-us/",
    "/ar/home/", "/ar/about-us/", "/ar/why-reval/", "/ar/services/",
    "/ar/industries/", "/ar/hse-sustainability/", "/ar/contact-us/", "/ar/join-us/",
]


def get_credentials():
    return service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)


def api_get(creds, path, params=None):
    creds.refresh(Request())
    r = requests.get(API + path, headers={"Authorization": "Bearer " + creds.token}, params=params, timeout=60)
    if r.status_code != 200:
        return None, r.status_code
    return r.json(), r.status_code


def api_post(creds, path, body):
    creds.refresh(Request())
    r = requests.post(API + path, headers={"Authorization": "Bearer " + creds.token}, json=body, timeout=60)
    if r.status_code != 200:
        return None, r.status_code
    return r.json(), r.status_code


def list_sites(creds):
    data, code = api_get(creds, "/sites")
    if data is None:
        print(f"[!] sites list failed HTTP {code}")
        return []
    return [s["siteUrl"] for s in data.get("siteEntry", [])]


def inspect(creds, site, url):
    body = {"inspectionUrl": url, "siteUrl": site, "languageCode": "en-US"}
    creds.refresh(Request())
    r = requests.post(API_V1 + "/urlInspection/index:inspect",
                      headers={"Authorization": "Bearer " + creds.token}, json=body, timeout=60)
    if r.status_code != 200:
        return {"error": r.status_code}
    res = r.json().get("inspectionResult", {})
    return res.get("indexStatusResult", {}) or {}


def sitemaps(creds, site):
    data, code = api_get(creds, "/sites/{}/sitemaps".format(site.replace("/", "%2F")))
    if data is None:
        print(f"[!] sitemaps failed HTTP {code}")
        return []
    return [{"path": s.get("path"), "lastSubmitted": s.get("lastSubmitted"),
             "lastDownloaded": s.get("lastDownloaded"), "isPending": s.get("isPending"),
             "errors": s.get("errors"), "warnings": s.get("warnings"),
             "contents": [(c.get("type"), c.get("submitted"), c.get("indexed")) for c in s.get("contents", [])]}
            for s in data.get("sitemap", [])]


def performance(creds, site, days=28):
    from datetime import date, timedelta
    body = {
        "startDate": (date.today() - timedelta(days=days)).isoformat(),
        "endDate": date.today().isoformat(),
        "dimensions": ["query"],
        "rowLimit": 20,
    }
    data, code = api_post(creds, "/sites/{}/searchAnalytics/query".format(site.replace("/", "%2F")), body)
    if data is None:
        print(f"[!] performance failed HTTP {code}")
        return []
    return data.get("rows", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--inspect", action="store_true")
    ap.add_argument("--performance", action="store_true")
    ap.add_argument("--sitemap", action="store_true")
    args = ap.parse_args()

    creds = get_credentials()
    sites = list_sites(creds)
    if not sites:
        print("لم يتم العثور على أي موقع. أضف المستخدم الخدمي في Search Console ثم أعد المحاولة.")
        sys.exit(1)

    global SITE
    SITE = next((s for s in sites if "reval-sa.com" in s), sites[0])
    print(f"== الموقع المختار: {SITE} ==")

    if args.performance or args.all:
        print("\n== الأداء (آخر 28 يومًا، أهم الكلمات) ==")
        rows = performance(creds, SITE)
        if not rows:
            print("  لا توجد بيانات بعد.")
        for row in rows:
            k = row.get("keys", [""])[0]
            print("  {:<40} {:<7} ظهور  {:<4} نقرة".format(k, row.get("impressions", 0), row.get("clicks", 0)))
        total_i = sum(r.get("impressions", 0) for r in rows)
        total_c = sum(r.get("clicks", 0) for r in rows)
        print(f"  المجموع: {total_i} ظهور / {total_c} نقرات (أهم 20 فقط)")

    if args.inspect or args.all:
        print("\n== فحص عناوين URL الرئيسية ==")
        for p in PAGES:
            url = PREFIX + p
            s = inspect(creds, SITE, url)
            state = s.get("coverageState", "?")
            verdict = s.get("verdict", "?")
            robots = s.get("robotsTxtState", "?")
            indexing = s.get("indexingState", "?")
            flag = " [اطلب الفهرسة]" if state in ("DISCOVERED", "NOT_INDEXED") else ""
            print("  {:<32} coverage={:<18} robots={:<8} {}".format(p, state, robots, flag))
            if state in ("DISCOVERED", "NOT_INDEXED"):
                print("      السبب: {}".format(s.get("coverageStateDescription", "-")))

    if args.sitemap or args.all or not (args.inspect or args.performance or args.sitemap or args.all):
        print("\n== ملفات خريطة الموقع ==")
        for s in sitemaps(creds, SITE):
            print("  {}".format(s["path"]))
            for t, sub, idx in s["contents"]:
                print("     {} مُقدّم: {} / مفهرس: {} ({})".format(t, sub, idx, "قيد المعالجة" if s["isPending"] else "مكتمل"))


if __name__ == "__main__":
    main()