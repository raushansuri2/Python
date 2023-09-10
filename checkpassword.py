def strength(password):
    check = []
    if len(password) > 7:
        check.append(True)
    else:
        check.append(False)
    upper = False
    digits = False
    for indes in password:
        if indes.isupper():
            upper = True
        elif indes.isdigit():
            digits = True

    check.append(upper)
    check.append(digits)
    return check;

che  = strength(input("enter the password"))
print(che)
if all(che):
    print("Password Strong")
else:
    print("Password weak")
