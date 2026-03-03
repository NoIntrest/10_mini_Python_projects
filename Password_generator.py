import string
import secrets
def generate_password(length = 16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

new_password = generate_password(16)
print(new_password)

