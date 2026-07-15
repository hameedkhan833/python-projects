# ---------------------TEMPERATURE CONVERTER--------------------------


print(" Type '1' for Celsius to Farenheit coverter  \n Type '2' for Farenheit to Celsius converter .  ")

# Celsius to Farenheit coverter;

user_inp = int(input("Enter : "))
if user_inp == 1:
    celc = float(input("Enter temperature in Celsius : "))
    F = (celc * 1.8) + 32
    print("Celcius to Farenheit : ",F,"°F") 

# Farenheit to Celsius converter;

elif user_inp == 2:
    Faren = float(input("Enter temperature in Farenheit : "))
    C =  (Faren - 32) / 1.8
    print("Farenheit to Celsius : ",C,"°C")     

else :
    print("Enter valid choice!")    