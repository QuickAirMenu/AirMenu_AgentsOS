# 📋 PROJECT PLAN — [Project Name]

> **Commander:** سشيي  
> **Lead Agent:** Dragon  
> **Last Updated:** [Date]  
> **Status:** 🔴 Planning / 🟡 In Progress / 🟢 Done

---

## 🎯 Project Overview

**What are we building?**  
[Short description — 2-3 sentences max]

**Who is the client?**  
[Client name, industry, location]

**What problem does it solve?**  
[The core problem this product addresses]

---

## 🏗️ Architecture Decision

**Backend:** Laravel [version]  
**Frontend:** React (Vite) + Tailwind / Plain HTML  
**Database:** MySQL  
**Auth:** Sanctum / Breeze / Custom  
**Hosting:** VPS / cPanel / Shared  
**Domain:** [domain.com]  
**Repo:** [github.com/username/repo]

**Reason for these choices:**  
[Why this stack was chosen for this specific project]

---

## 🗄️ Database Schema Summary

| Table        | Key Columns                   | Relations           |
|--------------|-------------------------------|---------------------|
| users        | id, name, phone, role         | has many bookings   |
| [table_2]    | ...                           | ...                 |

---

## 🗺️ Project Phases

### Phase 1 — Foundation
- [ ] Repo setup & branching strategy (Lion)
- [ ] Database schema design (Panther)
- [ ] Laravel project init + migrations (Wolf)
- [ ] Auth system (Wolf)
- [ ] Base API routes scaffold (Wolf)

### Phase 2 — Core Features
- [ ] [Feature 1] — Backend (Wolf) + Frontend (Fox)
- [ ] [Feature 2] — Backend (Wolf) + Frontend (Fox)
- [ ] [Feature 3] — Backend (Wolf) + Frontend (Fox)

### Phase 3 — Polish & QA
- [ ] Full code review (Hawk)
- [ ] Bug fixes from Hawk's report
- [ ] Performance audit (Panther)
- [ ] Responsive + RTL QA (Fox)

### Phase 4 — Deployment
- [ ] Staging environment setup (Lion)
- [ ] Production server config (Lion)
- [ ] SSL + domain config (Lion)
- [ ] Final deploy + smoke test

---

## 🔌 API Endpoints

| Method | Endpoint              | Auth | Agent | Status |
|--------|-----------------------|------|-------|--------|
| POST   | /api/v1/auth/login    | No   | Wolf  | ⬜     |
| GET    | /api/v1/users         | Yes  | Wolf  | ⬜     |
| ...    | ...                   | ...  | ...   | ...    |

---

## 🐛 Known Issues / Technical Debt

See `ISSUES.md` (maintained by Hawk)

---

## 📝 Session Log

### Session [Date]
**Goal:** ...  
**Completed:**  
- ...  
**Blocked by:**  
- ...  
**Next session:**  
- ...

---

## ⚙️ Environment Variables Required

```env
APP_NAME=
APP_ENV=
APP_KEY=
APP_URL=

DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=

MAIL_HOST=
MAIL_USERNAME=
MAIL_PASSWORD=

# Third-party APIs
WHATSAPP_API_KEY=
SMS_API_KEY=
PAYMENT_KEY=
```
