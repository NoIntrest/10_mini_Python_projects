import string
import secrets
def generate_password(length = 16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password
n = int(input("Set the length of the password: "))
new_password = generate_password(n)
print(new_password)
