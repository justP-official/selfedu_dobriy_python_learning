def validate_email(email):
    t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', '.'}

    if email.count("@") == 1 and email.count(".") >= 1 and email.count("_") >= 1:
        for c in email:
            if c in t:
                continue
            else:
                print("НЕТ")
                break
        else:
            print("ДА")
    else:
        print("НЕТ")


checked_email = input()

validate_email(checked_email)
