class Vendor:
    def __init__(self, inventory= None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 
    
    def get_by_id(self,item_id):
        for item in self.inventory: 
            if item.id == item_id:
                return item 
        return None 
    def swap_items(self,other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.remove(their_item)

        self.add(their_item)
        other_vendor.add(my_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False 
        
        first_vendor_item = self.inventory[0] 
        first_othervendor_item = other_vendor.inventory[0]

        self.inventory[0]= first_othervendor_item
        other_vendor.inventory[0] = first_vendor_item

        return True 
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category

    def get_best_by_category(self, category=None):
        items_in_category = self.get_by_category(category)

        if not items_in_category:
            return None 
        item_best_condition = items_in_category[0]
        for item in items_in_category:
            if item.condition > item_best_condition.condition:
                item_best_condition = item
        return item_best_condition     
            

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        
        if my_best_item is None or their_best_item is None:
            return False
        
        self.remove(my_best_item)
        other_vendor.add(my_best_item)
        
        other_vendor.remove(their_best_item)
        self.add(their_best_item)
        
        return True




        







