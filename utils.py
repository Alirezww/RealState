from constansts import SUPERVISOR_CREDENTIAL


def check_credentials(user_credentials):
    if len(user_credentials) > 2:
        username_check = bool(SUPERVISOR_CREDENTIAL[0]['username'] == user_credentials[1])
        password_check = bool(SUPERVISOR_CREDENTIAL[0]['password'] == user_credentials[2])
        return username_check, password_check
    return False
