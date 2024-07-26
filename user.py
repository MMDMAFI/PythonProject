
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"User({self.username})"

    @staticmethod
    def validate_user(users, username, password):
        for user in users:
            if user.username == username and user.password == password:
                return True
        return False
