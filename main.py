# Напиши класс, что принимает при инициализации user_email и сохраняет в атрибут класса.
# У него также есть метод send_email, который принимает message, берет user_email из
# атрибутов класса и принтит что-то типа 'Емейл отправлен на тут_емейл_юзера: тут_текст_из_message'
# Напиши дальше инициализацию с передачей емейла юзера, а потом вызовом send_email.

class Post:
    def __init__(self, content):
        self.content = content
        self.votes = 0  # Начальное количество голосов

    def upvote(self):
        self.votes += 1  # Увеличиваем количество голосов на 1

    def downvote(self):
        self.votes -= 1  # Уменьшаем количество голосов на 1

    def get_votes(self):
        return self.votes

# Пример использования
post = Post("Это пример поста.")
post.upvote()  # Голосование за пост
post.upvote()  # Еще одно голосование
post.upvote()  # Еще одно голосование
post.upvote()
post.upvote()  
post.upvote()


post.downvote()  # Голосование против поста
post.downvote()  # Голосование против поста
post.downvote()  # Голосование против поста
print(post.get_votes())  # Выведет: 1