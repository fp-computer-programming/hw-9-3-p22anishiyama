# Author: 1/13/22


def temp_convert(temp, temp_type):
    fahrenheit_math = (temp * 1.8) + 32
    fahrenheit_temp = "{0}°F".format(fahrenheit_math)
    celsius_math = (temp - 32) * 1.8
    celsius_temp = "{0}°C".format(celsius_math)
    try:
        if(temp_type == "f"):
            return celsius_temp
        elif(temp_type == "c"):
            return fahrenheit_temp
        else:
            return("Please only type either f or c.")
    except:
        return("Please try retyping your response.")

while True:
    temperature = float(input("Please input a temperature: "))
    temperature_type = input("°F or °C? ")
    print(temp_convert(temperature, temperature_type))
    response = input("Would you like to convert again? (Y/N) ")
    if(response.lower == "y"):
        continue
    elif(response.lower == "n"):
        break