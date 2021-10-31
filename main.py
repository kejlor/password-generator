import password


password_length = input("How long password do you require?\n")
generated_password = password.Password(password_length)
generated_password.generate_strong_password()
generated_password.print_password()
