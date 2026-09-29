import mpmath
import os

def calculate_and_save_pi(digits, filename="pi_digits.txt"):
    try:
        # بررسی ورودی
        if digits < 0:
            print("تعداد ارقام نمی‌تواند منفی باشد.")
            return

        # تنظیم دقت محاسبات (تعداد ارقام اعشار + ۵ رقم اضافه برای جلوگیری از خطای گرد کردن)
        mpmath.mp.dps = digits + 5 
        
        # محاسبه عدد پی با دقت تنظیم شده
        # علامت + قبل از mpmath.pi باعث می‌شود عدد با دقت جدید (dps) محاسبه و رفرش شود
        pi_value = +mpmath.pi 
        
        # تبدیل عدد به رشته متنی (digits + 1 چون خود عدد 3 هم یک رقم است)
        pi_str = mpmath.nstr(pi_value, digits + 1)
        
        # ذخیره در فایل
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"عدد پی تا {digits} رقم اعشار:\n\n")
            file.write(pi_str)
            
        print(f"عملیات با موفقیت انجام شد!")
        print(f"عدد پی تا {digits} رقم اعشار در فایل '{filename}' ذخیره شد.")
        
    except Exception as e:
        print(f"خطایی رخ داد: {e}")

if __name__ == "__main__":
    try:
        # دریافت ورودی از کاربر
        user_input = input("چند رقم از عدد پی را می‌خواهید محاسبه و ذخیره کنید؟ ")
        num_digits = int(user_input)
        
        calculate_and_save_pi(num_digits)
        
    except ValueError:
        print("لطفاً یک عدد صحیح و معتبر وارد کنید.")
