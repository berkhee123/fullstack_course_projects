data=[]
def add_item(item_id, name, **properties):
    if not item_id or not name:
        raise ValueError("item_id bolon name zaaval baih ystoi.")
    for item in data:
        if item["item_id"] == item_id:
            raise ValueError(f"{item_id}) ID-tai zuil ali hediin burtgegdsen baina.") 
    new_item = {"item_id": item_id, "name": name}
    new_item.update(properties)
    data.append(new_item)
    return new_item
student = add_item("S001", "Bold", age=20, grade="A", major="Computer Science")
print(student)
product = add_item("P001", "Notebook", price=1200000, brand="Dell", in_stock=True)
print(product)

def update_item(item_id, field, value):
    for item in data:
        if item ["item_id"] == item_id:
            if field in item:
                item[field] = value
                return True
            else:
                raise ValueError(f"{field} gedeg tailbar oldsongui")
                return False
success = update_item("S001", "age", 21)
print(success)
success = update_item("P001", "price", 1300000)
print(success)
success = update_item("X999", "name", "Baihgui zuil")
print(success)
def remove_item(item_id):
    for i, item in enumerate(data):
        if item["item_id"] == item_id:
            del data[i]
            return True
    return False
success = remove_item("S001")
print(success)
success = remove_item("S001")
print(success)


