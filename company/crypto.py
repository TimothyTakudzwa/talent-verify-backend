from django.db import models
from cryptography.fernet import Fernet
import os 

# Generate a secret key for encryption (you should keep this key secure and not hardcode it)
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

class EncryptedCharField(models.CharField):
    def from_db_value(self, value, expression, connection):
        try:
            decrypted_value = cipher_suite.decrypt(value.encode()).decode()
        except:
            decrypted_value = value
        return decrypted_value

    def to_python(self, value):
        try:
            decrypted_value = cipher_suite.decrypt(value.encode()).decode()
        except:
            decrypted_value = value
        return decrypted_value

    def get_prep_value(self, value):
        encrypted_value = cipher_suite.encrypt(value.encode()).decode()
        return encrypted_value



