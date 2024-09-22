# Dictionary full of info
data = {
    'name': "Veena Uppalapati",
    'age': 33,
    'hobbies': ['Photogaphy', 'Painting', 'Drawing'],
    'wakeup': {
        'Monday': "8:00 AM",
        'Tuesday': "8:30 AM",
        'Wednesday': "9:00 AM",
        'Thursday': "9:30 AM", 
        'Friday': "8:00 AM"
    }
    }

# Print out results stored in the dictionary
print(f"My name is {data['name']} and I am {data['age']} years old")
print(f"The first in my hobby list is {data['hobbies'][0]}")

# Use a loop to print out the key-value pairs in the dictionary
for key, value in data.items():
    print(f"key: {key}; value: {value}")


# Use a loop to print out the keys of the wake-up dictionary
for key in data['wakeup'].keys():
    print(F"Key: {key}")

# Use a loop to print out the values of the wake-up dictionary
for val in data['wakeup'].values():
    print(f"value: {val}")