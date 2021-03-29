from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()
    f = Fernet(key)
    filename = ('x.py')
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)