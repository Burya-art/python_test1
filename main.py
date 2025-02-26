class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution, new_title):
        self.resolution = new_resolution
        self.title = new_title


img = Image('1920x1080', "Sunset", "jpg")
print(img.resolution, img.title, img.extension)

img.resize('860x540', 'Night')
print(img.resolution)













# class Post:
#     def __init__(self, content):
#         self.content = content
#         self.votes = 0  # Начальное количество голосов
#
#     def upvote(self, qty):
#         self.votes += qty
#
#     def downvote(self):
#         self.votes -= 1  # Уменьшаем количество голосов на 1
#
#     def get_votes(self):
#         return self.votes
#
# # Пример использования
# post = Post("Это пример поста.")
# post.upvote(5)  # Голосование за пост
#
#
# post.downvote()  # Голосование против поста
# print(post.get_votes())  # Выведет: 1