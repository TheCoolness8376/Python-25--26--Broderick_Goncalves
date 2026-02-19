import math

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

    # Convert to Celsius first
    def Celsius_to_Fahrenheit(temp):
        return (temp * 9/5) + 32
    
    def Celsius_to_Kelvin(temp):
        return temp + 273.15
    
    # Add Fahrenheit_to_Kelvin
    # Add Fahrenheit_to_Celsius

    # Add Kelvin_to_Fahrenheit
    # Add Kelvin_to_Celsius
    
    # Celsius to target unit
    double = 0

    if (from_unit) == "C" and to_unit == "F":
        result = Celsius_to_Fahrenheit(temp)

    if (from_unit) == "C" and to_unit == "K":
        result = Celsius_to_Kelvin(temp)

    print(f"Result:{result:.2f}{to_unit}")

    choice = input("Convert again? (yes/no): ").lower()
    if choice == "no":
        running = False