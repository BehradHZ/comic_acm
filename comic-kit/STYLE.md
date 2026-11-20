# The Three Stones — Comic Kit Style

سبک تثبیت‌شده: **2D Ink + Cel + Pronounced Comic Halftone**. طرح‌ها باید به کمیک چاپی حرفه‌ای و مینی‌فیگور LEGO شبیه باشند، نه به مدل رندر سه‌بعدی.

## قواعد تصویری
- **تصویرسازی دوبعدی** با دورخط جوهری مشکیِ محکم و ضخیم و خطوط داخلیِ تمیز و کمتر ضخیم.
- رنگ‌گذاری تخت و گروه‌بندیِ سطوح روشن، میانه و تاریک به شیوهٔ **cel shading**، با رنگ‌های خانوادگی ثابت.
- **Ben-Day dots / comic dot texture کاملاً قابل‌مشاهده** روی مو، ردا، کیف، پارچه، پاها و سایه‌های متوسط؛ در لبه‌های تصویر و زمینه تراکم بیشتر و روی صورت و نقاط اتصال سنگ‌ها تراکم کمتر.
- صورت، دهان، چشم، برچسب و شکل سنگ **همواره خوانا** می‌مانند؛ اندازهٔ نقاط نباید خطوط جوهری را حذف یا چشم/دهان را پر کند.
- تمام شخصیت‌ها **LEGO classic minifigure anatomy** دارند: سر استوانه‌ای، تنهٔ صاف و بلوکی، پاهای دوگانهٔ مستطیلی و دست‌های C شکل **بدون انگشت**. سینهٔ زنانه فقط با چاپ سطحی بسیار کم القا می‌شود؛ هیچ برجستگی حجمی وجود ندارد.
- معماری، اجسام و حتی سازه‌های جنگی از قطعات LEGO ساخته شوند؛ وسایل طراحی‌شده باید اتصال مکانیکیِ قابل‌تصور داشته باشند.
- **Life:** قرمز/شرابی، چهرهٔ زنِ جاافتادهٔ حدود ۴۰ سال، موی شرابی، لب صاف، سرخیِ پس از گریه زیر چشم.
- **Wisdom:** آبی، چشم سفیدِ نورانی، موی/ریش سفید، دهان پشت ریش و سنگ آبی در عصای پیچ‌خورده.
- **Creation:** کرم/طلایی، جوان و مو نارنجی؛ سنگ زرد گردنبندی.
- **Farmers:** خاکی و وصله‌دار، بدون **زخم روی چهره**؛ Farmer 1 زنانه‌نما و عصبانی، Farmer 2 دخترِ موفرفری و Farmer 3 آرام و متفکر.
- **سنگ‌ها:** سه سیلوئت مستقل و ترکیب‌شونده از SVG مرجع، رنگ‌های زرد بالا/آبی پایین‌چپ/قرمز پایین‌راست. نه الماس عمومی، نه شش‌ضلعی منتظمِ تحمیلی.
- خداها با لباس‌های **ساده، خوش‌فرم و کم‌الگو** طراحی شوند: خطوط حاشیه و پنل‌های محدود، بدون نقش‌های ریشه/ستاره/مکعب متعدد و شلوغ.
- نورپردازی دراماتیک اما تخت و چاپی؛ بدون bloom زیاد، پوست/پارچهٔ واقع‌گرا، 3D rendering، painterly brushwork، نویز نامنظم و جزئیات اضافیِ نامرتبط.

## شیت مرجع
کاراکترها به ترتیب `LIFE / WISDOM / CREATION / FARMER 1 / FARMER 2 / FARMER 3` در یک ردیف با زمینهٔ عاجی، دانه‌های کمیکی نارنجی و خطوط رنگیِ کوتاه زیر نام‌ها هستند.

نسخهٔ تاریخی: [style-reference.png](style-reference.png) و [character-lineup-v01.png](characters/character-lineup-v01.png). مشخصات جاری: [characters/DESIGN_SYSTEM.md](characters/DESIGN_SYSTEM.md)، پرونده‌های هر شخصیت در [characters](characters/README.md) و [stones/STONES.md](stones/STONES.md). نسخهٔ جدید باید بر اساس مشخصات v02 و اصلاحات پس از تصویر آخر ساخته شود.

## Prompt پایه
```text
Clean 2D LEGO comic-book character illustration; classic rigid LEGO
minifigure proportions, cylindrical yellow heads, flat printed torsos,
authentic open C-claw hands without fingers, blocky LEGO legs, thick
confident black ink outlines, bold flat cel shading, strongly visible
traditional Ben-Day comic halftone dots in midtones and shadows,
vintage warm ivory dotted-paper background, subtle character acting,
readable expressions, fixed character hairstyles and costume shapes,
simple intentional god outfits, lightly patched war-worn farmer clothes
with uninjured faces, and faithful unique interlocking colored stones
with correct attachments (staff or necklace when specified).
No 3D render, no human anatomy, no protruding breasts, no extra gems,
no random decorative pattern noise, no photoreal hair, no fingers.
```
