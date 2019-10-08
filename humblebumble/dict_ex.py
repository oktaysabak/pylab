def displayInventory(inventory): 
    for k, v in inventory.items(): 
        print("{} {}".format(v, k)) 
    
    total_item  = sum( list(inventory.values()) ) 
    print("Total number of items: {}".format(total_item))

inventory = {'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, 'dagger':1 }

displayInventory(inventory)