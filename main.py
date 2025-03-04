# Напиши класс, что принимает при инициализации user_email и сохраняет в атрибут класса. У него также есть метод send_email, который принимает message, берет user_email из атрибутов класса и принтит что-то типа 'Емейл отправлен на тут_емейл_юзера: тут_текст_из_message'
# Напиши дальше инициализацию с передачей емейла юзера, а потом вызовом send_email.


class EmailSender:
    def __init__(self, user_email):
        self.user_email = user_email

    def send_email(self, message):
        print(f'Емейл отправлен на {self.user_email}: {message}')


send = EmailSender('new-email@gmail.com')
send.send_email('Hello!')








# Напиши класс, что ничего не принимает при инициализации, но создает атррибут класса _data(хай будет список). У класса должны быть следующие методы:
#     - add, который принимает value и добавляет его в конец _data, а конце метода принтит _data.
#         - если value уже есть в _data - рейзит ошибку что такое уже добавлено.
#     - remove, который принимает индекс элемента и удаляет его из списка по индексу, а конце метода принтит _data.
#         - если список _data пустой - рейзит ошибку что нельзя ничего удалить из пустого _data.
#     - do_print, который ничего не принимает, а просто в цикле принтит "индекс_элемента_в_списке: сам_элемент'
#         - если список _data пустой - рейзит ошибку что нельзя ничего принануть, бо список пустой.
# Инициализируй класс, а потом поиграйся с ним, повызывай методы, посмотри что будет и как работают.


class EmailSender:
    def __init__(self):
        self.data = [2, 5, 3]

    def add(self, value):
        try:
            if value in self.data:
                raise ValueError('Такое значение уже добавлено')
            self.data.append(value)
            print(self.data)
        except ValueError as e:
            print(e)

    def remove(self, index):
        try:
            if not self.data:
                raise ValueError("Нельзя ничего удалить из пустого data")
            self.data.pop(index)
            print(self.data)
        except ValueError as e:
            print(e)

    def do_print(self):
        if not self.data:
            raise ValueError('Список пустой')
        for index in range(len(self.data)):
            print(index)


email_send = EmailSender()

email_send.do_print()