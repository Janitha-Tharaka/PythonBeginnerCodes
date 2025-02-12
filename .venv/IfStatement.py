print("-------------If Statements-------------\n")

temperature = 50

if temperature > 45:
    print("It's a Radiation Day\n")
elif temperature > 30 and temperature <= 45:
    print("It's a Hot Day\n")
elif temperature > 20 and temperature <= 30:
    print("It's a Normal Day\n")
elif temperature > 10 and temperature <= 20:
    print("It's a Cold Day\n")
else:
    print("It's Freezing Day\n")

print('Temperature Showed Correctly')
