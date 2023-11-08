#Importa desde la libreria "Cryptodome.Cipher" el algoritmo de encriptacion "AES"
from Cryptodome.Cipher import AES
#Importa desde la libreria "Cryptodome.Util.Padding" las funciones "pad" y "unpad"
from Cryptodome.Util.Padding import pad,unpad
#Importa desde la libreria "base64" las funciones "b64encode" y "b64decode"
from base64 import b64encode, b64decode
def encrypt_message(message, key):
    key = key.encode('utf-8')
    cipher = AES.new(pad(key, AES.block_size), AES.MODE_ECB)
    encrypted_message = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return b64encode(encrypted_message).decode('utf-8')

def decrypt_message(message, key):
    key = key.encode('utf-8')
    cipher = AES.new(pad(key, AES.block_size), AES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(b64decode(message)), AES.block_size).decode('utf-8')
    return decrypted_message