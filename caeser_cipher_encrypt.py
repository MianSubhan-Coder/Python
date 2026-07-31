def caesar(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift

    shift = shift % 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet + alphabet.upper(), shifted + shifted.upper())
    return text.translate(table)

text = input("Enter your text: ")

try:
    shift = int(input("Enter the shift value: "))
    action = input("Type 'encrypt' or 'decrypt': ").strip().lower()

    if action == 'encrypt':
        print(f"Result: {caesar(text, shift, True)}")
    elif action == 'decrypt':
        print(f"Result: {caesar(text, shift, False)}")
    else:
        print("Invalid choice.")
except ValueError:
    print("The shift value must be an integer.")
