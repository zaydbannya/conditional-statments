def check_temperature(temp):
    if temp >= 30:
        return "It's hot! wear light clothes."
    elif temp <= 10:
        return "It's cold! wear warm clothes"
    else:
        return "It's moderate. wear regular clothes"

# Get temperature input from the user
temperature = float(input("Enter the temperature in Celsius: "))

# Print the appropriate message
print(check_temperature(temperature))