#Dasgal 1 
def add_item(item_id, name, **properties):


    age = properties.get('age', None)
    grade = properties.get('grade', None)
    major = properties.get('major', None)
    price = properties.get('price', None)
    brand = properties.get('brand', None)
    in_stock = properties.get('in_stock', None)
    students= [item_id, name, age, grade, major,]
    product = [item_id, name, price, brand, in_stock]
    if item_id.startswith("S"):      
        return(students)
    elif item_id.startswith("P"):
         return(product)
    else:
        print("item ID S, P ehleh ystoi")
ValueError:print("ID davdsarsan baina, shaardlagad niitseegui baina")
student = add_item("S001", "Bold", age=20, 
grade="A", major="Computer Science")
print(student)
product = add_item("P001", "Notebook", price=1200000, brand="Dell", in_stock=True)
print(product)





    


   



 