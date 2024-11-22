from cryptography.fernet import Fernet


#encryption key generation in a binary file
def generate_file_key() -> bool:
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as file:
        file.write(key)
    return True

def load_key():
    #read in binary (rb")
    return open("encryption.key", "rb").read()


def encrypt(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode()) #encode in bytes before encrypting
    return encrypted_message



def decrypt(message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(message)
    decrypted_message = decrypted_message.decode() # convert from bytes to string
    return decrypted_message
