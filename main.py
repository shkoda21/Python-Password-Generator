import string
import random


def gen_password(len_password):
    password = ''
    password += random.choice(string.ascii_lowercase) + \
                random.choice(string.ascii_uppercase) + \
                random.choice(string.digits) + \
                random.choice(string.punctuation)
    for j in range(len_password - 4):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password


while True:
    try:
        len_password = int(input('Write the password length, number must be  between 8 and 16    '))
        if 8 <= len_password <= 16:
            print(gen_password(len_password))
            break
        else:
            print('Please, write the number between 8 and 16')
    except ValueError as err:
        print(err)

