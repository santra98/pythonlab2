import string
from random import *
char = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(char)for x in range(randint(8,13)))
print(password)