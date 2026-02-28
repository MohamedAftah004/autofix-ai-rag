def validate_answer(answer: str) -> tuple[bool, str]:
    hallucination_signals = [
        "غالباً",
        "ممكن",
        "قد يكون",
        "أعتقد",
        "في الأغلب"
    ]

    for signal in hallucination_signals:
        if signal in answer:
            return False, "الرد فيه استنتاج أو هبد مش موجود في الداتا"

    return True, ""