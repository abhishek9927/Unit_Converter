def length_converter():
    print("\nLength Converter (meters <-> kilometers)")
    val = float(input("Enter value in meter: "))
    print(f"{val} meters = {val / 1000} kilometers")
    print(f"{val} meters = {val * 100} centimeters")
    print(f"{val} metres = {val / 1000} litres")

def weight_converter():
    print("\nWeight Converter (kilogram <-> grams)")
    val = float(input("Enter value in kilograms: "))
    print(f"{val} kg = {val * 1000} grams")


def temperature_converter():
    print("\nTemperature Converter (Celsius <-> Fahrenheit)")
    c = float(input("Enter temperature in celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")

def main():
    while True:
        print("\n---Basic Unit Converter ---")            
        print("1. Length COnverter")
        print("2. Weight Converter")
        print("3 Weight Converter")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again. ")

if __name__ == "__main__":
    main()           