def sarcastic_capitalization(text):
    final_message = ""
    for letter in text:
        if text.index(letter) % 2 == 0:
            new_letter = letter.replace(letter, letter.capitalize())
            final_message += new_letter
        else:
            final_message += letter
    return final_message
