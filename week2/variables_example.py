# 1. Numeric Types
age = 25                    # Integer (int)

price = 19.99               # Floating point (float)
# 2. Text Type

name = "Gemini"             # String (str)

# 3. Boolean Type
is_coding = True            # Boolean (bool)

# 4. Sequence Types
skills = ["Python", "AI"]   # List (mutable collection)

coordinates = (10, 20)      # Tuple (immutable collection)

# 5. Mapping Type Dictionary (key-value pairs)
user_info = { "role": "Assistant", "active": True
}

# --- Utilizing the data ---

# Displaying information and checking types

print(f"User: {name}")
print(f"Age: {age} | Type: {type(age)}")
print(f"Price: ${price} | Type: {type(price)}")

# Logic using a Boolean
if is_coding:
    print(f"{name} is currently working with {skills[0]}.")

# Accessing a dictionary
print(f"Current Role: {user_info['role']}")
