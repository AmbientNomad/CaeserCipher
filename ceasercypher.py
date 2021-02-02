alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decoder(user_message, cypher):
    message_list = [letter for letter in user_message]
    solved_list = []

    for x in message_list:

        if x.isalpha():
            change_index = alphabet.index(x.lower()) + cypher

            if change_index < 0:
                change_index = len(alphabet) - abs(change_index)
            elif change_index > len(alphabet) - 1:
                change_index = change_index - len(alphabet)

            if x.isupper():
                solved_list.append(alphabet[change_index].upper())
            else:
                solved_list.append(alphabet[change_index])

        else:
            solved_list.append(x)
            
    message_solved = "".join(solved_list)
    return message_solved


message = input("What message would you like to alter? ")
shift_number = int(input("Enter a number, 1-25 (positive or negative), to shift the message "))

while abs(shift_number) not in range(1, 26):
    print("That's not an option.")
    shift_number = int(input("Enter a number, 1-25, to shift the message "))

print(decoder(message, shift_number))
