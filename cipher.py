# Input sentence
text = input('Please enter a sentence:')

# Input how many letters you want to shift
shift = int(input('How many letters do you want to shift? (Must be in the range of 0 - 26)'))

# Input which direction you want to shift
direction = input('Which direction do you want to shift?: (Right or Left?)')

# Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Direction 
if direction.lower() == "right":
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
elif direction.lower() == "left":
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift]

# Create the alphabet dictionary with shifted values
cipher_dict = {alphabet[i]: shifted_alphabet[i] for i in range(26)}
cipher_dict.update({alphabet[i].upper(): shifted_alphabet[i].upper() for i in range(26)})

# Print the cipher dictionary for verification
print("Cipher Dictionary:", cipher_dict)

# Encrypt/Decrypt the text
result = ""
for char in text:
    if char in cipher_dict:
        result += cipher_dict[char]
    else:
        result += char

# Output the result
print("Encryption:", result)