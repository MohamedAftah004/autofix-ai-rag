def validate_answer(answer: str):
    if not answer or len(answer) < 30:
        return False, "الرد غير كافي"

    return True, None