alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decoder(user_message, cypher):
    message_list = [letter for letter in user_message]  # Splits our message to solve letter by letter
    solved_list = []  # Will store our converted letters before saving as a new message

    for character in message_list:

        if character.isalpha():  # Need to confirm character is a letter, 'else' it returns that character

            # Variable and if statement for determining which letter of the alphabet will be swapped
            change_index = alphabet.index(character.lower()) + cypher
            if change_index < 0:
                change_index = len(alphabet) - abs(change_index)
            elif change_index > len(alphabet) - 1:
                change_index = change_index - len(alphabet)

            if character.isupper():  # Simple check to determine upper case or lower case replacement
                solved_list.append(alphabet[change_index].upper())
            else:
                solved_list.append(alphabet[change_index])

        else:
            solved_list.append(character)

    return "".join(solved_list)  # Combines our altered message for printing


message = input("What message would you like to alter? ")
# Allows user to enter any message, encrypted or not. Can be any message, but only A-Z characters will be shifted.

shift_number = int(input("Enter a number, 1-25 (positive or negative), to shift the message "))
# Number required to alter message. 25 max because 26 will result in no change.
while abs(shift_number) not in range(1, 26):  # Prevent user from entering an unusable shift number
    print("That's not an option.")
    shift_number = int(input("Enter a number, 1-25, to shift the message "))

print(message)
print(decoder(message, shift_number))
