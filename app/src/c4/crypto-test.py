# pip install pycryptodome
import Crypto
from Crypto.Cipher import AES

message = 'foobarfoobar'
password = 'rocket'

def aes_new(password, iv):
    sha = Crypto.Hash.SHA256.new()
    sha.update(password.encode())
    return AES.new(sha.digest(), AES.MODE_CFB, iv)

def encrypt(data, password):
    iv = Crypto.Random.new().read(AES.block_size)
    print(aes_new(password, iv))
    return iv + aes_new(password, iv).encrypt(data)

def decrypt(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return aes_new(password, iv).decrypt(cipher)

enc = encrypt(message, password)
dec = decrypt(enc, password)

print("encrypted: ", enc)
print("decrypted: ", dec)