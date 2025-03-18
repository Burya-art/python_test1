class CreateMessageMixin:
    def create_message(self):
        return f"Возвращает сообщение"


class ValidateUserMixin:
    ALLOW_USERS = [1, 2, 3]
    def validate_user(self, user_id):
        if user_id not in self.ALLOW_USERS:
            raise ValueError("юзер айди нету в списке разрешенных юзеров")


class MailSender(CreateMessageMixin, ValidateUserMixin):
    def __init__(self, user_id):
        self.validate_user(user_id)
        self.user_id = user_id

    def send_message(self):
        print(self.create_message())


sender = MailSender(3)
sender.send_message()