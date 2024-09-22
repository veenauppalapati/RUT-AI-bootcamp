
# Python Cheat Sheet

* `input()` - prompts the user to type an input value in

### Type Casting

* `int()` `str()` `float()` `bool()`

* Printing multiple items: `print("The sum of 5 + 3 is:", 5 + 3)`

* Concatenation: `print("Hello " + name)`

* Printing with formatted strings (f-string literals): `print(f"{name} is {age} years old")`

* printing string multiple times: `print(string_variable * 5)`


`\` is an escape character you can use to include a quotation mark in the string without it being taken as a part of the overall function

`\n` new line

### String Manipulation

`upper()` converts a string to UPPERCASE

`lower()` converts a string to lowercase

`title()` converts a string to Title Case

### Multiline f-string
print(f"Text {variable}. More text\n"
    + f"Text: {calculation}\n")

### Formatting numbers
f'{value:{width},.{precision}}'

## Data Structures

### Slicing

* `info_list = ["Samar", 25, "Kyra", 20]`

* `info_list[start: stop]` - Select items from the start index to the stop index.

* `info_list[start:]` - select items from the start index to the end of the list.

* `info_list[:stop]` - select items up to the stop index.

* `info_list[:]` - select all items in the list

### List Functions 

* `index(element)` - returns the index (position) of the element

* `append(element)` - method adds elements to the end of a list

* `pop(index)` - removes a value by index, and stores it into the variable

* `remove(element)` - removes a given value from a list

* `len(list)` - returns the length of a list.

* `max(list)` - returns the maximum value in the list.

* `min(list)` - returns the minimum value in the list.

* `sum(list)` - adds all numbers in the list together

## Tuples

Lists 

- can be modified after declaration

- defined with `[]`

Tuples 

- cannot be modified after declaration.

- defined with `()`

## Input Validation

* `.isdigit()` - returns ture if it's an int else False

## Identity operators 





