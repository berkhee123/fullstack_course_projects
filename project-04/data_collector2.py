# Dasgal 2
 
items = {
    "S001": {"item_id": "S0001", "field": 500, "value": 0},
    "P001": {"item_id": "P0001", "field": 600, "value": 10,}
}

def update_item(item_id, field, value):
   
    if item_id in items:
        if field in items[item_id]:
            items[item_id][field] = value
            return True
        else:
            raise ValueError(f"'{field}' gedeg talbar oldsongui.")
    else:
        return False

success = update_item("S001", "field", 20)
success1= update_item("S001", "value", 21)
print(success, success1)  

success = update_item("P001", "value", 1300000)
success1= update_item("P001", "field", 21)
print(success)  

success = update_item("X999", "name", "baihgui zuil")
print(success)  
print(items) 
