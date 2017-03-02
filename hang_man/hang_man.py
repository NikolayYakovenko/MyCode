import getpass

class HangMan():
    GAME_STEPS = 5
    USER_LIVES = 5

    @classmethod
    def game_procces(cls):
        user_word = cls.ask_user_to_type_word()
        partly_visible_word = ['*'] * len(user_word)
        asterisks_list = cls.make_asterisks_from_word(user_word)
        asterisks_list = ''.join(asterisks_list)
        user_lives_count = None

        print('Word to guess: {}\n'.format(asterisks_list))

        for step in range(cls.GAME_STEPS):
            if step == 0:
                user_lives_count = cls.USER_LIVES

            user_letter = cls.ask_user_to_type_letter(user_lives_count)
            guessed_letters = cls.show_guessed_letters(user_word, user_letter)

            if not user_letter or user_letter not in user_word:
                user_lives_count -= 1

            # save all guessed letters and show it on next steps
            for i, symbol in enumerate(guessed_letters):
                if symbol != '*':
                    partly_visible_word[i] = partly_visible_word[i].replace(partly_visible_word[i], symbol)

            result = ''.join(partly_visible_word)

            if user_word == result:
                return print('\nYou win the game!\nThis word is - {}.'.format(user_word))
            elif step == cls.GAME_STEPS or user_lives_count == 0:
                return print('Game over!')
            else:
                print('\nWord to guess: {}'.format(result))

    @classmethod
    def ask_user_to_type_word(cls):
        word = getpass.getpass(prompt='Type a word and press Enter: ')
        return word.lower()


    @classmethod
    def ask_user_to_type_letter(cls, lives):
        next_letter = input('You have {} lives left - Letter? '.format(lives))
        return next_letter.lower()


    @classmethod
    def make_list_from_word(cls, word):
        letters = []
        for letter in word:
            letters.append(letter)
        return letters


    @classmethod
    def make_asterisks_from_word(cls, word):
        asterisks = list(map(lambda letter: letter.replace(letter, '*'), word))
        return asterisks


    @classmethod
    def show_guessed_letters(cls, word, user_letter):
        if user_letter in word:
            guessed_letters = cls.replace_asterisk_on_letter(word, user_letter)
            return guessed_letters
        else:
            return []


    @classmethod
    def replace_asterisk_on_letter(cls, word, next_letter):
        user_word_list = cls.make_list_from_word(word)
        asterisks_list = cls.make_asterisks_from_word(word)
        letter_positions = []

        # get letter position in word and replace asterisk on this letter
        for index, symbol in enumerate(user_word_list):
            if symbol == next_letter:
                letter_positions.append(index)

        for i in letter_positions:
            asterisks_list[i] = next_letter

        return asterisks_list


HangMan.game_procces()
