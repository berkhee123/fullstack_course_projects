# Хөрвүүлэх томъёонууд:

# Цельсээс Фаренгейт руу хувиргах
# def celsius_to_fahrenheit(celsius):
# return (celsius * 9/5) + 32

# Фаренгейтээс Цельс рүү хувиргах
# def fahrenheit_to_celsius(fahrenheit):
    # return (fahrenheit - 32) * 5/9

# Кельвин (K) 
# def celsius_to_kelvin(c):
#   return c + 273.15

# Жишээ:
# c = 25
# f = celsius_to_fahrenheit(c)
# print(f"{c}°C = {f:.2f}°F")

# f = 77
# c = fahrenheit_to_celsius(f)
# print(f"{f}°F = {c:.2f}°C")
# print("Ta C, F, K 3-iin negiig butsaana uu!")

# Кельвин (K) 
# def celsius_to_kelvin(c):
#   return c + 273.15

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

print("Температур хөрвүүлэгч программ (гарах бол 'exit' гэж бичнэ үү)")

while True:
    temparutur_type = input("Та C, F, K гурвын нэгийг оруулна уу ('exit' бол гарах): ").upper()
    
    if temparutur_type == "EXIT":
        print("Программыг хааж байна...")
        break

    if temparutur_type not in ['C', 'F', 'K']:
        print("Алдаа: Та зөвхөн 'C', 'F', 'K' гэсэн үсэг оруулна уу.")
        continue

    try:
        temparutur = float(input("Та хөрвүүлэх температурын тоогоо оруулна уу: "))
    except ValueError:
        print("Алдаа: Та зөвхөн тоон утга оруулна уу!")
        continue

    if temparutur_type == "K" and temparutur < 0:
        print("Кельвин температур нь 0-ээс бага байж болохгүй!")
        continue

    if temparutur_type == "C":
        kelvin_value = celsius_to_kelvin(temparutur)
        if kelvin_value < 0:
            print("Алдаа: Цельс утга нь -273.15-аас бага байж болохгүй!")
            continue
        print(f"{temparutur}°C = {celsius_to_fahrenheit(temparutur):.2f}°F")
        print(f"{temparutur}°C = {kelvin_value:.2f}K")

    elif temparutur_type == "F":
        kelvin_value = fahrenheit_to_kelvin(temparutur)
        if kelvin_value < 0:
            print("Алдаа: Энэ Фаренгейт утга Кельвин рүү хөрвүүлэхэд 0-ээс бага болж байна!")
            continue
        print(f"{temparutur}°F = {fahrenheit_to_celsius(temparutur):.2f}°C")
        print(f"{temparutur}°F = {kelvin_value:.2f}K")

    elif temparutur_type == "K":
        print(f"{temparutur}K = {kelvin_to_celsius(temparutur):.2f}°C")
        print(f"{temparutur}K = {kelvin_to_fahrenheit(temparutur):.2f}°F")

    print("--------------------------------------------------")
