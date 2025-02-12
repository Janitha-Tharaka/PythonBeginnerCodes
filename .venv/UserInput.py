print("-------------User Inputs-------------\n")

first_name = input("Enter Your Name: ")
first_num = input("Enter First Number: ")
second_num = input("Enter Second Number: ")

total = float(first_num) + float(second_num)

print(f"Hi {first_name}, Your Total is {total}\n")

print("-------------Remove Decimals-------------\n")

decimal_total = round(float(first_num) + float(second_num), 2)

print(f"Your Two Decimal Total is {decimal_total}\n")

print("-------------Remove Decimals New-------------\n")

print(f"Your New Two Decimal Total is {total:.2f}\n")


