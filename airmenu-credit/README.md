# AirMenu Credit

سكريبت جاهز يُدرج تلقائيًا "Developed By Air Menu Co." في أي مشروع — مع رسالة راقية في Console عند فتح أدوات المطوّر (F12).

Reusable drop-in credit for "Developed By Air Menu Co." — injects the footer credit and a branded console message in any project, with no styling conflicts.

## التركيب / Usage

أضف سطرًا واحدًا قبل إغلاق `</body>` في أي صفحة:

```html
<script src="https://cdn.jsdelivr.net/gh/QuickAirMenu/AirMenu_AgentsOS@main/airmenu-credit/airmenu-credit.min.js"></script>
```

## الخيارات / Options (كلها اختيارية)

| السمة | الوظيفة |
|---|---|
| `data-airmenu-link` | رابط بديل (الافتراضي: `https://airmenu.net/contact`) |
| `data-airmenu-target` | مُحدّد لوضع الـ credit في عنصر محدد بدل `footer` |
| `data-airmenu-no-console` | ضع القيمة `"1"` لإخفاء رسالة الـ Console |

### مثال متقدم:

```html
<script
  src="https://cdn.jsdelivr.net/gh/QuickAirMenu/AirMenu_AgentsOS@main/airmenu-credit/airmenu-credit.min.js"
  data-airmenu-link="https://airmenu.net/contact"
  data-airmenu-target="#my-footer"
  data-airmenu-no-console="0"
></script>
```

## ماذا يفعل / What it does

1. **الفوتر:** أضاف عنصر `<p class="airmenu-credit">Developed By <a>Air Menu Co.</a></p>` داخل `footer` (أو الهدف المحدد) — برباط مفتوح في تبويب جديد مع `rel="noopener noreferrer"`.
2. **التنسيق:** يحقن CSS خاصًا معزولًا (لا يتعارض مع أنماط موقعك) مع اتجاه `LTR` لضمان ترتيب صحيح في الصفحات العربية (RTL).
3. **Console:** عند فتح F12 تعرض رسالة الهوية الرقمية لـ Air Menu بألوان العلامة.

## تطوير / Development

- `airmenu-credit.js` — المصدر القابل للقراءة.
- `airmenu-credit.min.js` — النسخة المضغوطة المستخدمة في الإنتاج (استخدمها عبر jsDelivr).
