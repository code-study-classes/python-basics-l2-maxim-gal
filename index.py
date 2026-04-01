def update_profile(user_id, **updated_fields):
    return {"id": user_id, "updated_fields": updated_fields}


def get_domains(emails):
    return [email.split("@")[1] for email in emails]


def filter_target_audience(users):
    return [
        user for user in users
        if user.get("age", 0) >= 18 and user.get("is_premium") is True
    ]

 build_response(status_code, *errors, **payload):
    return {"status": status_code, "errors": errors, "data": payload}


def calculate_total_spent(transactions):
    return sum(txn.get("amount", 0) for txn in transactions)