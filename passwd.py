import string
from random import *

caracteres = string.ascii_letters + string.punctuation + string.digits
passwd = "".join(choice(caracteres)
                 for x in range(randint(12, 24)))  # Altere os números para ter maior complexidade de senha

print("Sua senha é:", passwd)
