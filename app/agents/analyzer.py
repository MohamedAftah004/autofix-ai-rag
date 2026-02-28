def analyze_input(description: str, car_model: str):
    keywords = [
        "عربية", "سيارة", "موتور", "تكييف", "فرامل",
        "دركسيون", "فتيس", "بطارية", "كهربا" , "الأنوار"
    ]

    if not any(k in description for k in keywords):
        raise ValueError("الوصف لا يخص أعطال سيارات")

    return {
        "description": description.strip(),
        "car_model": car_model.strip()
    }