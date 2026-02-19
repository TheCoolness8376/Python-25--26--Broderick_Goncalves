print("Temperatuer Converter")
print("Units: C = Celsius, F = Fahrenheit, K = Kelvin")

running = True

while running:
    try:
        temp = float(input("Enter temperture values: "))
    except:
        print("Invalid number. Please enter a numeric value.")

    from_unit = input("Enter input with (C/F/K): ").upper()
    to_unit = input("Enter input unit (C/F/K): ").upper()

    # Validate the units
    if from_unit not in ["C", "F", "K"] or to_unit not in ["C", "F", "K"]:
        print("Invalid unit. Please use C, F, or K.")

    # Kelvin cannot be negative
    if from_unit == "K" and temp < 0:
        print("Invalid: Kelvin cannot be negative.")
        continue

    # Convert input to Celsius first
    if from_unit == "C":
        celsius = temp
    elif from_unit == "F":
        celsius = (temp - 32) * 9/5 # Celsius to Fahrenheit
    elif from_unit == "K":
        celsius = temp * 273.15 # Celsius to Kelvin

    # if from_unit == "F":
    #     fahrenheit = temp
    # elif from_unit == "C":
    #     fahrenheit = (temp - 32) * 5/9 # Fahrenheit to Celsius
    # elif from_unit == "K":
    #     fahrenheit = (temp - 32) * 5/9 + 273.15 # Fahrenheit to Kelvin
    
    # Celsius to target unit
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = (celsius * 9/5) + 32
    elif to_unit == "K":
        result = celsius * 273.15

    print(f"Result: {result:.2f}{to_unit}")

    choice = input("Convert again? (yes/no): ").lower()
    if choice == "no":
        running = False
    