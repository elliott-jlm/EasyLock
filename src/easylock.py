import preprocess

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

    boolean,dictionary = preprocess.check_sentence(sentence)

    # checking the validity of the input sentence
    while not boolean:
        print('\nPlease, enter a new sentence that respect the following rules :\n')
        for key,value in dictionary.items():
            if value == False:
                print('   - ' + key + ' : ❌\n')
            else:
                print('   - ' + key + ' : ✅\n')
        sentence = input()
        boolean, dictionary = preprocess.check_sentence(sentence)

    # split the sentence in words
    words = sentence.split(' ')

    password_parts = []
    for word in words:
        password_parts.append(preprocess.choose_relevant_letters(word))
    password = ''.join(password_parts)
    print("\n\nVoici votre mot de passe : \n")
    return password

def main():
    print("Pour générer votre mot de passe, tapez une phrase dont vous vous souviendrez. \
        \nCette phrase doit contenir au moins :\n\
           - 12 mots.\n\
           - 1 lettre majuscule au début d'un des mots.\n\
           - 1 lettre minuscule.\n\
           - 1 chiffre.\n\
           - 1 caractère spécial : !”#$%&’()*+,-./:;<=>?@[\]^_`{|}~\n\n")

    sentence = input()
    password = password_generator(sentence)
    print(password)

main()