import string
from art import logo

alphabets = [a for a in string.ascii_lowercase]


# Function to encode text
def encode(text: str, shift=3) -> str:
    output_text = ""
    for letter in text:
        if letter.isalpha():
            index = (alphabets.index(letter) + shift) % 26
            output_text += alphabets[index]
        else:
            output_text += letter

    return output_text


# Function to decode text
def decode(text: str, shift=3) -> str:
    output_text = ""
    for letter in text:
        if letter.isalpha():
            index = alphabets.index(letter) - shift
            index = index if index >= 0 else index + 26
            output_text += alphabets[index]
        else:
            output_text += letter

    return output_text


is_on = True
# Print Logo
print(logo)

while is_on:
    # Ask user for choice
    user_choice = input("\nEnter your choice \nEncrypt: e\nDecrypt: d\n")
    input_text = None

    if user_choice.lower().startswith("e"):
        input_text = input("Enter your text: ").lower()
        output = encode(input_text)
        print("Encrypted Text: ", output)

    elif user_choice.lower().startswith("d"):
        input_text = input("Enter your text: ").lower()
        output = decode(input_text)
        print("Decrypted Text: ", output)

    else:
        print("Invalid Option.")
        continue

    continue_using = input("Continue using PySecurity? Y or N: ")
    if continue_using.lower().startswith("y"):
        continue
    else:
        is_on = False
        print("Thanks for using PySecurity. We value your privacy the most!")
