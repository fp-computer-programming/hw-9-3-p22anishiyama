# Author: 1/13/22

# temperature = input("Please input a temperature: ")
# temperature_type = input("Fahrenheit or celsius? ")

def temp_convert(temp, temp_type):
    fahrenheit_math = (temp * 1.8) + 32
    fahrenheit_temp = "{0}°F".format(fahrenheit_math)
    try:
        if(temp_type.lower == "celsius"):
            return fahrenheit_temp
        elif(temp_type.lower == "fahrenheit"):
            return celsius_temp
    except:
        print("an error occured")

temp_convert(40, "celsius")
