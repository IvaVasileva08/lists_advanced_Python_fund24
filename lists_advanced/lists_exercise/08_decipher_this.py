secret_message = input()
def code_message(message):
    text = message.split()
    code_words = []

    for word in text:
        num_str = ''.join([char for char in word if char.isdigit()])
        first_letter = chr(int(num_str))
        rest_of_word = word[len(num_str):]
        if len(rest_of_word) > 1:
            rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
        code_word = first_letter + rest_of_word
        code_words.append(code_word)
    return ' '.join(code_words)
code_message = code_message(secret_message)
print(code_message)