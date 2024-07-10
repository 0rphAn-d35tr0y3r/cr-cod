import sys
import pyzipper

output_path = "./"

password = "tryme"
output_path = "C:\Temp"

def brute_force():
    for i in range(1000):
        password = str(i).zfill(3)

        try:
            with pyzipper.AESZipFile("attachments/secret.zip") as zip_file:
                zip_file.setpassword(password.encode())
                zip_file.extractall(path=output_path)
                print(f"Password: {password}")
                return password
        except (RuntimeError, pyzipper.BadZipFile):
            continue
    print("Sorry we cannot find the password")

    
if __name__ == "__main__":
    print("This are ")