letters = ['a', 'o', 'u', 'e', 'i']
letters_text = input()
letters_list = [letter for letter in letters_text if letter.lower() not in letters]
print (''.join(letters_list))