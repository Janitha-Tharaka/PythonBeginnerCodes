
print("-------------Weight Conversion App-------------\n")

user_weight = input("Please insert your Weight: ")

try:
    user_weight = float(user_weight)  # Convert to float
except ValueError:
    raise SystemExit("You have entered a wrong value for Weight. Please run this again!")

user_weight_symbol = input("Please type if the entered weight is Kg(K) or Lbs(L). (Use K or L): ")

try:
    user_weight_symbol = str(user_weight_symbol).lower()

    if (user_weight_symbol == 'k'):
        user_converted_weight = float(user_weight) * 2.205;
        user_converted_weight_symbol = 'Lbs'

    elif (user_weight_symbol == 'l'):
        user_converted_weight = float(user_weight) / 2.205;
        user_converted_weight_symbol = 'Kg'

    else:
        raise SystemExit("You have entered a wrong value for Weight. Please run this again!")

    print(f"The Weight of yours is {round(float(user_converted_weight), 2)} in {user_converted_weight_symbol}")

except ValueError:
    raise SystemExit("You have entered a wrong value for Symbol. Please run this again!")


