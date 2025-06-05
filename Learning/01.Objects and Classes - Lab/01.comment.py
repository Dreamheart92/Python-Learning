class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment('David', 'I like this book', 0)

print(comment.username)
print(comment.likes)
print(comment.content)
