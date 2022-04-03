import zipfile
from random import randint
import string

def crack_password(obj):
    guess = ""
    characters = string.ascii_letters + string.punctuation + "0987654321"
    pwd_list = []
    while True:
        guess = ""
        for n in range(6,11):
            for letter in range(n):
                guess_letter = characters[randint(0, 25)]
                guess = str(guess_letter) + str(guess)
            if guess in pwd_list:
                guess = ""
                continue
            pwd_list.append(guess)
            try:
                obj.extractall(pwd=guess)
                print("Password is", guess.decode())
                return True
            except:
                print(f"Password '{guess}' does not match.")
                guess = ""
                continue

zip_file = "Folder.zip"
obj = zipfile.ZipFile(zip_file)
if crack_password(obj):
	print("Password was found")
    
