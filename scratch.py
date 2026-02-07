fruits = ["apple", "banana"]
fruits.append("cherry")      # ["apple", "banana", "cherry"]
fruits.insert(1, "orange")   # ["apple", "orange", "banana", "cherry"]
fruits.extend(["mango", "kiwi"])

nums = [10, 20, 30, 20]
nums.remove(20) # [10, 30, 20] (only the first 20 is gone)
last = nums.pop() # Removes 20, last = 20, nums = [10, 30]
nums.pop(0) # Removes index 0 with a value of 10

chars = ["b", "a", "d", "c"]
chars.sort()    # ["a", "b", "c", "d"]
chars.reverse() # ["d", "c", "b", "a"]

vals = [1, 2, 2, 3, 2]
print(vals.count(2)) # Output: 3
print(vals.index(3)) # Output: 3

user_stats = {"health": 100, "mana": 50}

# .get() - Returns None if key is missing (instead of crashing)
stamina = user_stats.get("stamina") 
print(f"Stamina: {stamina}") # Output: None
# print(f"Stamina: {user_stats["stamina"]}") # would work if key exists otherwise, KeyError exception

# .get() with a default value
strength = user_stats.get("strength", 10) 
print(f"Strength: {strength}") # Output: 10

inventory = {"apples": 5, "bananas": 2, "oranges": 8}

# .keys() - All the labels
print(inventory.keys())   # dict_keys(['apples', 'bananas', 'oranges'])
for k in inventory.keys():
    print(k)

# .values() - All the data
print(inventory.values()) # dict_values([5, 2, 8])

# .items() - Key and Value pairs (perfect for loops)
for fruit, count in inventory.items():
    print(f"We have {count} {fruit}")

settings = {"theme": "dark", "notifications": True}

# .update() - Merge another dictionary or add new keys
settings.update({"theme": "light", "font_size": 14})
# Result: {'theme': 'light', 'notifications': True, 'font_size': 14}

settings["theme"] = "light" # changes "theme key to "light"

# .setdefault() - Inserts key only if it DOESN'T exist
settings.setdefault("language", "English") # Adds it
settings.setdefault("theme", "blue")        # Does nothing because "theme" exists

cart = {"item1": "Laptop", "item2": "Mouse", "item3": "Monitor"}

# .pop() - Removes a specific key and returns the value
removed_item = cart.pop("item2")
print(f"Removed: {removed_item}") # Output: Mouse

# .popitem() - Removes the last inserted item
last_added = cart.popitem()
print(f"Last item removed: {last_added}") # Output: ('item3', 'Monitor')

# .clear() - Wipes the dictionary clean
cart.clear()
print(cart) # Output: {}