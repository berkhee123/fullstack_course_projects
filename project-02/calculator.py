def tses ():
    print("\n=== Тооны Машин Цэс ===")
    print("1. Нэмэх")
    print("2. Хасах")
    print("3. Үржүүлэх")
    print("4. Хуваах")
    print("0. Гарах")

def calculator ():
    while True:
        tses ()
        choice = input("Үйлдлээ сонгоно уу (0-4): ")

        if choice == "0":
            print("Программыг хаалаа.")
            break

        if choice in ["1", "2", "3", "4"]:
            a = float(input("Эхний тоо: "))
            b = float(input("Хоёр дахь тоо: "))

            if choice == "1":
                print("Нэмэх үр дүн:", a + b)
            elif choice == "2":
                print("Хасах үр дүн:", a - b)
            elif choice == "3":
                print("Үржүүлэх үр дүн:", a * b)
            elif choice == "4":
                if b == 0:
                    print("Алдаа: 0-ээр хувааж болохгүй!")
                else:
                    print("Хуваах үр дүн:", a / b)

        else: 
            print("Буруу сонголт, Дахин оролдоно уу.")
       
calculator ()
       