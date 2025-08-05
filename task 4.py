ef celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def kilometers_to_miles(kilometers):
    return kilometers * 0.621371
def miles_to_kilometers(miles):
    return miles / 0.621371
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462
def pounds_to_kilograms(pounds):
    return pounds / 2.20462
conversions = {
    '1': {'name': 'Celsius to Fahrenheit', 'function': celsius_to_fahrenheit},
    '2': {'name': 'Fahrenheit to Celsius', 'function': fahrenheit_to_celsius},
    '3': {'name': 'Kilometers to Miles', 'function': kilometers_to_miles},
    '4': {'name': 'Miles to Kilometers', 'function': miles_to_kilometers},
    '5': {'name': 'Kilograms to Pounds', 'function': kilograms_to_pounds},
    '6': {'name': 'Pounds to Kilograms', 'function': pounds_to_kilograms},
}
def display_menu():
    print("\nUnit Conversion Menu:")
    for key, value in conversions.items():
        print(f"{key}. {value['name']}")
    print("7. Exit")
def get_conversion_choice():
    while True:
        choice = input("Enter the number of your choice: ")
        if choice in conversions:
            return choice
        elif choice == '7':
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
def get_value():
    while True:
        try:
            value = float(input("Enter the value to convert: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def main():
    while True:
        display_menu()
        choice = get_conversion_choice()
        if choice == '7':
            print("Exiting the program.")
            break
        else:
            conversion = conversions[choice]
            value = get_value()
            result = conversion['function'](value)
            print(f"{value} -> {result} ({conversion['name']})")

if __name__ == "__main__":
    main()
