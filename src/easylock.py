import re


def contains_1_number(sentence):
    """
    Checking if the sentense contains at least one number.
    """
    pattern = ".*[0-9].*"
    if re.search(pattern, sentence):
        return True
    else:
        return False


def contains_1_lowercase_letter(sentence):
    """
    Checking if the sentense contains at least one lowercase letter.
    """    
    pattern = '.*[a-z].*'
    if re.search(pattern, sentence):
        return True
    else:
        return False


def contains_1_capital_letter(sentence):
    """
    Checking if the sentense contains at least one capital letter in first position of a word.
    """
    pattern = '^[A-Z]'
    c = 0
    words = sentence.split(' ')
    for word in words:
        if c == 0:
            if re.search(pattern, word):
                c+=1
    if c == 1:
        return True
    else:
        return False


def contains_1_special_caracter(sentence):
    """
    Checking if the sentense contains at least one a special character.
    """
    pattern = ".*[!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~].*"
    if re.search(pattern, sentence):
        return True
    else:
        return False


def check_sentence(sentence):
    """
    Checking if the sentense respect the five rules.
    """
    defects = {'12 words':False,
                '1 capital letter in first position of a word':False,
                '1 lowercase letter':False,
                '1 number':False,
                '1 special caracter':False
            }
    c = 0
    if len(sentence.split(' ')) >= 12:
        defects['12 words'] = True
        c+=1
    if contains_1_capital_letter(sentence):
        defects['1 capital letter'] = True
        c+=1
    if contains_1_lowercase_letter(sentence):
        defects['1 lowercase letter'] = True
        c+=1
    if contains_1_number(sentence):
        defects['1 number'] = True
        c+=1
    if contains_1_special_caracter(sentence):
        defects['1 special caracter'] = True
        c+=1
    
    if c == 5:
        return True,defects
    else:
        return False,defects


def detect_special_characters(sentence):
    """
    Detect the special characters index
    """
    indexs = []
    pattern = "[!\"#$%&’\'()*+,-./:;<=>?@[\\]^_`{|}~]"
    for i in range(1,len(sentence)):
        if re.search(pattern, sentence[i]):
            indexs.append(i)

    return indexs


def detect_numbers(sentence):
    """
    Detect the numbers index
    """
    indexs = []
    pattern = "[0-9]"
    for i in range(1,len(sentence)):
        if re.search(pattern, sentence[i]):
            indexs.append(i)

    return indexs


def choose_relevant_letters(word):
    """
    Taking the first letter of the word and keep numbers and special characters.
    """
    relevant_letters = []
    first_letter = word[0]
    special_characters = detect_special_characters(word)
    numbers = detect_numbers(word)

    relevant_letters.append(first_letter)
    temp = sorted(special_characters + numbers)
    for index in temp:
        relevant_letters.append(word[index])

    return "".join(relevant_letters)


def password_generator(sentence):
    """
    This function generate a password with a sentence gives in parameter
    The sentence must have at least :
        - 12 words.
        - 1 capital letter in the first position of a word.
        - 1 lowercase letter.
        - 1 number.
        - 1 special character : !”#$%&’()*+,-./:;<=>?@[\]^_`{|}~
    """

    boolean,dictionary = check_sentence(sentence)

    # checking the validity of the input sentence
    while not boolean:
        print('\nPlease, enter a new sentence that respect the following rules :\n')
        for key,value in dictionary.items():
            if value == False:
                print('   - ' + key + ' : ❌\n')
            else:
                print('   - ' + key + ' : ✅\n')
        sentence = input()
        boolean, dictionary = check_sentence(sentence)

    # split the sentence in words
    words = sentence.split(' ')

    password_parts = []
    for word in words:
        password_parts.append(choose_relevant_letters(word))
    password = ''.join(password_parts)

    return password