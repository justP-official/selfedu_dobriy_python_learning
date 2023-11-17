def check_password(password, chars='$%!?@#'):
    f = False

    if len(password) > 8:
        for c in password:
            if c in chars:
                f = True
                return f
    return f
