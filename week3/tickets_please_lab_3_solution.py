# Lab 3 Solution
# Variables to test
age = 25
has_student_id = True
is_holiday = False
discount = False

# 1. Using 'and' with comparison operators
# Must be at least 18 AND have a student ID
# -- age >= 18 and age <= 60 and student --
if age >= 18 and has_student_id:
    discount = True
    print("Eligible for the Student Discount.")

# 2. Using 'or' with comparison operators
# Eligible if younger than 12 OR older than 65
# -- age < 10 or age > 60 --
elif age < 10 or age > 60: # rate changed
    print("Eligible for the Junior/Senior rate.")
    discount = True

# 3. Using 'not' to reverse logic
# Only proceed if it is NOT a holiday
if not is_holiday:
    print("Regular weekday pricing is active.")

# 4. Combining all three
# Eligible for a special promotion if:
# (Age is between 18 and 30 inclusive) AND (It is not a holiday)
if (age >= 18 and age <= 30) and not is_holiday:
    print("You qualify for the 'Young Adult' weekday special!")
    discount = True

# 5. Lab 3 Change
if 12 <= age < 18 and not has_student_id:
    print("Eligible for high school rate")
    discount = True

# if no discount credited above
if not discount:
    print("Standard ticket rate applies.")
    