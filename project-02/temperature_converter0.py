def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temparutur_type = str(input("Ta C, F, K 3-iin negiig butsaana uu!")).upper()

try:
    temparutur = float(input("Ta too oruulna uu"))  # Тоон утга эсэхийг шалгах
    print(temparutur)
    

except ValueError:  
    print("Та зөвхөн тоон утга оруулна уу!") # int биш байх юм бол хариулах алдааны мсж



if temparutur_type == "C":
    
    print(f"{temparutur}°C = {celsius_to_fahrenheit(temparutur):.2f}°F")
    print(f"{temparutur}°C = {celsius_to_kelvin(temparutur):.2f}K")

elif temparutur_type == "F":
   
    print(f"{temparutur}°F = {fahrenheit_to_celsius(temparutur):.2f}°C")
    print(f"{temparutur}°F = {fahrenheit_to_kelvin(temparutur):.2f}K")

elif temparutur_type == "K":
   
    print(f"{temparutur}K = {kelvin_to_celsius(temparutur):.2f}°C")
    print(f"{temparutur}K = {kelvin_to_fahrenheit(temparutur):.2f}°F")
else:
    print("Ta buruu useg oruulsan baina")




 




