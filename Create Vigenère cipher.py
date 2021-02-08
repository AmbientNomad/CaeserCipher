alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decoder(user_message, cipher):
    solved_list = []  # Will store our converted letters before saving as a new message
    cipher_pointer = 0  # Used for advancing through our cipher, to avoid additional loops

    for character in user_message:
        if character.isalpha():  # Need to confirm character is a letter, 'else' it returns that character

            shifted_index = alphabet.index(character.lower())
            # Used for creating our altered alphabet, stored in a variable to make the following lines easier to read
            shifted_alphabet = [letter for letter in alphabet[shifted_index:]]

            if shifted_index != 0:
                # For any letter other than A, will add the beginning letters of the alphabet, in order, to our shifted
                # alphabet
                shifted_alphabet.extend(letter for letter in alphabet[:shifted_index])

            swap_letter = shifted_alphabet[alphabet.index(cipher[cipher_pointer].lower())]

            if character.isupper():  # Simple check to determine upper case or lower case replacement
                solved_list.append(swap_letter.upper())
            else:
                solved_list.append(swap_letter)

            if cipher_pointer == len(cipher) - 1:
                # Will check to see if our cipher advances to the next letter, or resets to the first letter
                cipher_pointer = 0
            else:
                cipher_pointer += 1

        else:
            solved_list.append(character)

    return "".join(solved_list)  # Combines our altered message for printing


message = input("What message would you like to alter? ")
# Allows user to enter any message, encrypted or not. Can be any message, but only A-Z characters will be shifted.

cipher_word = input("Please enter a cipher, letters only, no spaces: ")
# While our message can handle characters and spaces, the script currently won't work if the cipher has them
while not cipher_word.isalpha():  # Prevent user from entering an unusable characters
    print("That's not an option.")
    cipher_word = input("Please enter a cipher, letters only, no spaces: ")

print(message)
print(decoder(message, cipher_word))
