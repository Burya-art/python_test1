with open('passwords.txt', 'r', encoding='utf-8') as file:
    passwords = [line.strip() for line in file]

used_passwords = []

class User:

    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 4:
            raise ValueError("Длина пароля слишком мала, минимум должно быть 4 символа")
        if len(value) > 12:
            raise ValueError("Длина пароля слишком велика, максимум должно быть 12 символов")
        try:
            if value in passwords:
                raise ValueError("Это слишком лёгкий пароль")
        except ValueError as e:
            print(e)

        self.__password = value
        used_passwords.append(value)


r = User('aaa', 123)

new_password = input("Введите пароль: ")

r.password = new_password
print(used_passwords)