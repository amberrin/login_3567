logins={
    "login"}
password={"3567"}
h = 0
a = input("Введіть логін: (Додати новий логін - s)")
if a == "s":
    f = input("Введіть новий логін:")
    logins = [f]
    o = input("Введіть новий пароль:")
    password = [o]
    print("Ваш логін був добавлен у базу даних")
    x = input("Введіть логін щоб війти")
    if x in logins:
        l = input("Введіть пароль")
        if l in password:
            print("Ви війшли у систему")
elif a in logins:
    b = input("Введіть пароль:")
    if b in password:
        print("Ви війшли")
    else:
        print("Помилка! Пароль введено не вірно")
else:
    print("Помилка! Такого логіна не існує")
    v = input("Додати новий логін - s")
    if v == "s":
        f = input("Введіть новий логін:")
        logins = [f]
        o = input("Введіть новий пароль:")
        password = [o]
        print("Ваш логін був добавлен у базу даних")
        x = input("Введіть логін щоб війти")
        if x in logins:
            l = input("Введіть пароль")
            if l in password:
                print("Ви війшли у систему")
