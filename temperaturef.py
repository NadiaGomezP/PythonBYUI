#FAHRENHEIT WINDCHILL


# F = (ºC . 1,8) + 32
# WIND CHILL = 35.74 + 0.6215 T - 35.75(V0.16) + 0.4275T(V0.16)
# TEMPARATURE INPUT = What is the temperature? 
# DEGREE INPUT (IF) = Fahrenheit or Celsius (F/C)? F
# PRINT = At temperature (temperature/to_fahrenheit), and wind speed (x) mph, the windchill is: (windchill_f/c)F

def windchill(T,V):
    windchill = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V **0.16)
    return windchill

def to_fahrenheit(temperature):
    celsius_to_fahrenheit = float(temperature * 9/5) + 32
    return celsius_to_fahrenheit

quit = ""

while quit.upper() != "Y":
    temperature = float(input("What is the temperature? "))
    temperature_degree = input("Fahrenheit or Celsius (F/C)? ")

    if temperature_degree.upper() == "F":
        for x in range(5, 65 ,5):
            windchill_f = windchill(temperature, x)
            print(f"At temperature {temperature:.1f}°F, and wind speed {x} mph, the windchill is: {windchill_f:.2f}°F")

    elif temperature_degree.upper() == "C":
        for x in range(5, 65 ,5):
            windchill_c = windchill(to_fahrenheit(temperature), x)
            print(f"At temperature {to_fahrenheit(temperature):.1f}°F, and wind speed {x} mph, the windchill is: {windchill_c:.2f}°F")

    quit = input("Do you want to quit? (Y/N) ")

