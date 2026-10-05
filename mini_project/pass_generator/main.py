import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("تعداد کاراکترهای رمز عبور را وارد کنید: "))
    
    if password_length < 8:
        print("رمز عبور باید حداقل 8 کاراکتر داشته باشد.")
    else:
        password = generate_password(password_length)
        print("رمز عبور تولید شده: ", password)
