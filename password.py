import random
import string


class Password:
    def __init__(self, password_length, generated_password=None):
        self.password_length = password_length
        self.generated_password = generated_password

    def generate_strong_password(self):
        password_option = string.digits + string.ascii_letters + string.punctuation
        self.generated_password = ''.join(random.choice(password_option) for i in range(int(self.password_length)))

    def print_password(self):
        print(f"Your generated password is: {self.generated_password}")
