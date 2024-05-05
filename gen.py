import random
import string

def generate_password():
    length = random.randint(15, 25)
    special_characters = '&%$#@!'
    characters = string.ascii_letters + special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Your generated password is:", password)
