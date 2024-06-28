# Print "hello world" to the console
print("hello world")

# Function to convert a string to its numerical form based on a phone dial pad
def text_to_numerical(text):
    dial_pad = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9',
        ' ': '0'
    }
    numerical_form = ''.join(dial_pad[char] for char in text.lower())
    return numerical_form

# Convert "hello world" to its numerical form
hello_world_numerical = text_to_numerical("hello world")
print("Numerical form of 'hello world':", hello_world_numerical)

# Ask for new numerical input from the user
new_numerical_input = input("Enter numbers to be converted to text (like a phone dial pad): ")

# Function to convert numerical input back to text based on a phone dial pad
def numerical_to_text(numerical):
    reverse_dial_pad = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': [' ']
    }
    text_output = []
    for digit in numerical:
        # For simplicity, we'll just take the first letter corresponding to the digit
        if digit in reverse_dial_pad:
            text_output.append(reverse_dial_pad[digit][0])
    return ''.join(text_output)

# Convert the new numerical input to text
converted_text = numerical_to_text(new_numerical_input)
print("Converted text:", converted_text)
