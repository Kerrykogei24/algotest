from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(data, DES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def des_decrypt(key, encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, DES.block_size)
    return unpadded_data

if __name__ == "__main__":
    key = get_random_bytes(8)
    data = b"Hello, DES!"

    encrypted_data = des_encrypt(key, data)
    decrypted_data = des_decrypt(key, encrypted_data)

    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)
