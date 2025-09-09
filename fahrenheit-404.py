user_input = input(f"Welcome to Fahrenheit 404: The Temperature Rebellion, what would you like to do? 1. Convert Celsius to Fahrenheit or 2. Convert Fahrenheit to Celsius. Enter your choice 1 or 2:")
if user_input == "1": 
    cel = float(input(f"you entered {user_input}, Celcius, Please input the Celcuis Value"))
    Fahern = (cel * 1.8) + 32
    print(f"your Celcius value in Fahrenheit is {Fahern}°F")
elif user_input == "2":
    fah = float(input(f"you entered {user_input}, Fahrenheit, Please input the Fahrenheit Value"))
    
    Celcius = (fah - 32) * .5555
    print(f"Your Fahrenheit value in Celcius is {Celcius}°C")
else:
    print(f"{user_input} was not 1 or 2, please reset.")