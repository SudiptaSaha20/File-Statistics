word = 0
alpha = 0
digit = 0
num = 0
alphanum = 0
special = 0
space = 0
line = 0

print("\033c")

filename = input(
    "Enter the file name or path (including the file extension, e.g., .txt). Ensure the file is in the same folder as this program if only the file name is provided: "
)

try:
    with open(filename, "r") as f:  # Open the file
        for x in f:  # x is a line in the file
            line += 1
            for i in range(len(x)):  # Iterate over the line 'x'
                if x[i].isalpha():  # Check if the character is alphabet
                    alpha += 1
                elif x[i].isdigit():  # Check if the character is numeric
                    digit += 1
                elif x[i].isspace():  # Check for spaces
                    space += 1
                else:
                    special += 1  # Count everything else (punctuation)

            words = x.split()  # Split line into words
            for word_str in words:
                word_str = word_str.strip(
                    ",.?;:/\"\\'()!<>+-*_^%$#@|[]{}="
                ).lower()  # Remove punctuation
                if word_str.isalpha():  # Count pure words (only alphabets)
                    word += 1
                elif word_str.isdigit():  # Count pure numbers (only digits)
                    num += 1
                elif word_str.isalnum():  # Count alphanumerics (digits + alphabets)
                    alphanum += 1

except FileNotFoundError:
    print("File not found. Please check the file name/path and try again.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

print(f"Lines: {line}")
print(f"Words (pure alphabets): {word}")
print(f"Numbers (pure digits): {num}")
print(f"Alphabets: {alpha}")
print(f"Digits: {digit}")
print(f"Alphanumerics: {alphanum}")
print(f"Special Characters: {special}")
print(f"Spaces: {space}")
print(f"Total Characters (including spaces): {alpha + digit + space + special}")

output = open("output.txt", "w")
output.write(
    f"Lines: {line}\nWords (pure alphabets): {word}\nNumbers (pure digits): {num}\nAlphabets: {alpha}\nDigits: {digit}\nAlphanumerics: {alphanum}\nSpecial Characters: {special}\nSpaces: {space}\nTotal Characters (including spaces): {alpha + digit + space + special}"
)
