class UserValidator:
    def __init__(self):
        with open("names.csv", "r") as f:
            self.users  = f.read().splitlines()

    def check_name(self, name):
        for user in self.users:
            args = user.split(",")
            if args[0] == name:
                return True
        return False

    def check_email(self, email):
        for user in self.users:
            args = user.split(",")
            if args[2] == email:
                return True
        return False

    def check_password(self, password):
        for user in self.users:
            args = user.split(",")
            if args[1] == password:
                return True
        return False