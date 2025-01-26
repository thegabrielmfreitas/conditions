age = input("Enter your age: ")

# Validate the input to ensure it's a non-negative integer
if not age.isdigit():
    print("Please enter a valid positive number for age.")
else:
    age = int(age)

    # Determine their age category
    category = ""
    if age < 0:
        category = "invalid age"
    elif age <= 4:
        category = "baby"
    elif age <= 12:
        category = "child"
    elif age <= 18:
        category = "teen"
    elif age <= 65:
        category = "adult"
    else:
        category = "elder"

    print(f"At the age of {age}, you are a {category}.")
