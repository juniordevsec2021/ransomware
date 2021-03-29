import glob
from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()
    f = Fernet(key)
for filename in glob.iglob('/home/**/*.enc', recursive=True):
    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
        decrypted = f.decrypt(encrypted)
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
