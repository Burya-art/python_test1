class BaseMailSender:
    def __init__(self, user_id, subscription_type):
        self.user_id = user_id
        self.subscription_type = subscription_type

    def create_message(self):
        raise NotImplementedError

    def send_message(self):
        print(self.create_message())


class FreeUserMailSender(BaseMailSender):
    def create_message(self):
        return f"name: {self.user_id}, Free: {self.subscription_type}"


class PremiumUserMailSender(BaseMailSender):
    def create_message(self):
        return f"name: {self.user_id}, Premium: {self.subscription_type}"


free = FreeUserMailSender('Ihor', 'Basic')
premium = PremiumUserMailSender('Ivan', 'Pro')

free.send_message()
premium.send_message()






















































