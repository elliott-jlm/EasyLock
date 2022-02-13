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


def contains_1_capital_letter(sentence):
    """
    Checking if the sentense contains at least one capital letter.
    """
    pattern = '.*[A-Z].*'
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


def contains_1_special_caracter(sentence):
    """
    Checking if the sentense contains at least one a special character.
    """
    pattern = ".*[!”#$%&’()*+,-./:;<=>?@[\\]^_`{|}~].*"
    if re.search(pattern, sentence):
        return True
    else:
        return False


def check_sentence(sentence):
    defects = {'12 words':False,
                '1 capital letter':False,
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


def password_generator(sentence):

    """
    This function generate a password with a sentence gives in parameter
    The sentence must have at least :
        - 12 words.
        - 1 capital letter.
        - 1 lowercase letter.
        - 1 number.
        - 1 special character : !”#$%&’()*+,-./:;<=>?@[\]^_`{|}~
    """

    boolean,dictionary = check_sentence(sentence)
    while not boolean:
        print('\nPlease, enter a new sentence that respect the following rules :\n')
        for key,value in dictionary.items():
            if value == False:
                print('   - ' + key + ' : ❌\n')
            else:
                print('   - ' + key + ' : ✅\n')
        sentence = input()
        boolean, dictionary = check_sentence(sentence)

    split_list = sentence.split(' ')
    first_letter = []
    for el in split_list:
        first_letter.append(el[0])
    password = ''.join(first_letter)

    return password

test = sentence_password_generator('elliott Joliman claude dominique $tanley 19 10 2000 guadeloupe marie galante grand bourg')
print('Your password is :\n\n   - ' + test + '\n\n')