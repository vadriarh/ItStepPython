def convert_user_to_json(user):
    return {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "years": user.years
    }


def convert_list_to_json(users_list: list = None):
    return [convert_user_to_json(user) for user in users_list or []]


def convert_error_to_json(error: str, details: str):
    return {"error": error, "details": details}

def get_userinfo_from_json(request):
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    return username, password