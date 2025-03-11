# Создайте класс User, который:
# 	•	Имеет приватные атрибуты _username (имя пользователя) и _password (пароль).
# 	•	Реализует метод set_password(old_password, new_password), который меняет пароль, но только если передан правильный старый пароль.
# 	•	Реализует метод get_username(), который возвращает имя пользователя.
# 📌 Дополнительно:
# 	•	Попробуйте изменить _password напрямую вне класса. Почему это плохо?
# 	•	Добавьте метод check_password(password), который проверяет, совпадает ли переданный пароль с сохраненным.

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def set_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            print("Password changed.")
        else:
            print("Password not changed.")

    def get_username(self):
        print(f"Username: {self.__username}")

    def check_password(self, password):
        if self.__password == password:
            print("Passwords match.")
            return True
        else:
            print("Passwords do not match.")
            return False

    def _show_password(self):  # защищённый метод, предназначенный для контроля содержимого пароля
        print(f"password: {self.__password}")


# Test Data
user = User("anton", "Yuuer")

user._show_password()
user.set_password("Uyww", "Uyww")
user._show_password()
user.check_password("Yuuer")
user.check_password("Uyww")
user.set_password("Yuuer", "Uyww")
user._show_password()
user.check_password("Yuuer")
user.check_password("Uyww")

user.get_username()

user.__password = "qwd"  # Создается новый публичный атрибут
print(user.__password)  # публичный атрибут, print не имеет доступа к приватному атрибуту __password
user._show_password()  # приватный атрибут внутри класса остался прежним
