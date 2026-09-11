# 🤝 REVAL Operations — Client

> عميل: شركة REVAL لإدارة العمليات (رفال) · `reval-sa.com`
> العقد: دعم فني 3 أشهر — المدة 3/2026-07-28
> المسؤول: Ahmed Mansour (Admin@AirMenu.net)

## الملفات
| الملف | الوصف |
|------|-------|
| `REVAL-متابعة-فهرسة-جوجل.html` | قائمة متابعة فهرسة Google (تفاعلية — تُفتح في المتصفح) |
| `REVAL-Audit-Report-Status.html` | حالة تدقيق الموقع |
| `REVAL-قائمة-المهام.html` | قائمة المهام العامة (19+ مكتمل + بنود المتابعة) |
| `REVAL-نطاق-العمل.html` | توزيع النطاق والتكلفة |
| `REVAL-الدعم-الفني.html` | نطاق الدعم الفني |
| `gsc_monitor.py` | مراقبة Search Console تلقائية (تغطية + أداء + sitemap) |
| `reval-old-url-redirects.php` | توجيه 301 للروابط القديمة (مثبّت في mu-plugins) |

## أداة المراقبة
```
python gsc_monitor.py --all
```
- يتطلب: `google-auth` + `requests` + ملف مفتاح حساب الخدمة
- المفتاح: `athman-arbaa-*.json` (خدمي، غير مرفوع هنا — سرّي)

## حالة الفهرسة (2026-09-11)
- مفهرسة: `/` ، `/join-us/` ، `/ar/industries/` ، `/ar/join-us/`
- المطلوب إجراء طلبات فهرسة: 12 صفحة (انظر القائمة التفاعلية)
- sitemap: 16 صفحة معتمدة بنجاح (10/09/2026)