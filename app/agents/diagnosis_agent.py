from app.llm.client import call_llm

def build_prompt(record: dict) -> str:
    return f"""
أنت ميكانيكي سيارات خبرة سنين في مصر.

ممنوع:
- تخترع أسباب
- تضيف حلول من عندك
- تستخدم أي معرفة غير اللي جاية في الداتا

⚠️ التزام صارم:
- متستخدمش أي معلومة غير المكتوبة تحت
- لو الحل مش واضح، قول إن البيانات غير كافية
- متخمنش

مهم جدًا:
لو البيانات مش كافية أو المشكلة غير مطابقة للداتا،
قول صراحة: "المعلومة دي غير متوفرة عندي" ومتحاولش تفسر. 

المطلوب:
اشرح الحل بالتفصيل وباللهجة المصرية، كأنك بتكلم صاحب العربية.

نوع العربية: {record['car_type']}
العطل: {record['fault']}
وصف المشكلة: {record['description']}
الحل من الداتا: {record['solution']}
مستوى الصعوبة: {record.get('difficulty', 'غير معروف')}
"""

def run_diagnosis(record: dict) -> str:
    prompt = build_prompt(record)
    return call_llm(prompt)