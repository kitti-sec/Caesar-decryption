def is_it_a_letter(new_key, letter):
    alpha = "ABCDEFGHIJKLMNOPQRSTUWXYZ"

    if letter in alpha:
        return alpha[new_key]
    else:
        return letter

def decrypt(key, text):
    text = text.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    result = ""

    for letter in text:
        new_key = (alphabet.find(letter) + key) % len(alphabet)
        result = result + is_it_a_letter(new_key, letter)

    return result

print("Caesar - Intelligence class.\n")
text = input("Input the text you want to decrypt: ").upper()
print()
# version 1 key = int(input("Enter key to decrypt: "))
key =0
for i in range(25):
    key = i
    print(decrypt(key,text))

input("Press enter to exit")