logins={
    "login"}
password={"3567"}
h = 0
a = input("Введіть логін:")
i = input("Додати новий логін - s")
if a in logins:
    b = input("Введіть пароль:")
    if b in password:
        print("Ви війшли")
    else:
        print("Помилка! Пароль введено не вірно")
else:
    print("Помилка! Такого логіна не існує")