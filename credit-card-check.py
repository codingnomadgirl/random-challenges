card_number = input("Enter your card number: ")


def card_check():
    if not int(card_number):  # correct this
        print("Please enter a number.")
    elif len(card_number) != 16:
        print("Card number incorrect. Please double check, it must be 16 digits.")
    else:
        hidden_card_number = []
        last_four_dgt = (card_number)[-4:]
        i = 0
        for number in card_number[:12]:
            i += 1
            hidden_card_number = i * '*'
        print(f"Your card number is {hidden_card_number}{last_four_dgt}.")


card_check()

# could use for different length challenges (len(card_number) - 4)
