def code(filename, to_file):
    code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..',
                 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                 '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..'}

    if to_file:
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                text = file.read()
        except IOError:
            print(f'Cannot open input file: {filename}')
            exit(1)
        name_of_file = input(f'Name an output file (without extension): ')
        try:
            with open(f'{name_of_file}.txt', 'w') as file:
                flag = 0
                for index, letter in enumerate(text):
                    letter = letter.upper()
                    if letter == '\n':
                        file.write('\n')
                        flag = 0
                    elif letter in code_dict.keys():
                        file.write(code_dict[letter])
                        file.write(' ')
                        flag = 1
                    elif letter == ' ' and flag:
                        file.write('/')
                        file.write(' ')
                        flag = 0
                    else:
                        raise ValueError(f'Input file {filename} contains: {letter}, at index: {index}. '
                                         f'This sign is not supported.')
        except IOError:
            print(f'Cannot open output file: {name_of_file}.txt')
            exit(1)
    else:
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                text = file.read()
        except IOError:
            print(f'Cannot open input file: {filename}')
            exit(1)
        flag = False
        for index, letter in enumerate(text):
            letter = letter.upper()
            if letter == '\n':
                print('')
                flag = True
            elif letter in code_dict.keys():
                print(code_dict[letter], end=' ')
                flag = True
            elif letter == ' ' and flag:
                print('/', end=' ')
                flag = False
            else:
                raise ValueError(f'Input file {filename} contains: {letter}, at index: {index}. '
                                 f'This sign is not supported.')


def code_gui(txt_frame, morse_frame):
    code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..',
                 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                 '8': '---..', '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..'}
    morse_frame.delete(1.0, 'end')
    text = txt_frame.get(1.0, 'end')
    flag = False
    for index, letter in enumerate(text):
        letter = letter.upper()
        if letter == '\n':
            morse_frame.insert('end', '\n')
            flag = True
        elif letter in code_dict.keys():
            morse_frame.insert('end', f'{code_dict[letter]} ')
            flag = True
        elif letter == ' ' and flag:
            morse_frame.insert('end', '/ ')
            flag = False
        else:
            morse_frame.insert('end', f'\nUNSUPPORTED SIGN: {letter}, AT INDEX: {index}')
            return


def decode(filename, to_file):
    mdict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
             '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
             '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
             '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
             '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-.-.-': '.', '--..--': ',',
             '..--..': '?'}

    if to_file:
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                data = file.read()
        except IOError:
            print(f'Cannot open input file: {filename}')
            exit(1)
        name_of_file = input(f'Name an output file (without extension): ')
        try:
            with open(f'{name_of_file}.txt', 'w') as file:
                new_word = True
                beginning = 0
                for i in range(0, len(data)):
                    if data[i] == '\\' or data[i] == '/':
                        new_word = True
                        file.write(' ')
                    elif data[i] == '\n':
                        if new_word is False:
                            file.write(mdict[str(data[beginning:i])])
                        new_word = True
                        file.write('\n')
                    elif data[i] == '.' or data[i] == '-':
                        if new_word:
                            beginning = i
                            new_word = False
                    elif data[i] == ' ':
                        if new_word is False:
                            new_word = True
                            file.write(mdict[str(data[beginning:i])])
                    else:
                        raise ValueError(f'File contains {data[i]} at index: {i}. Cannot decode.')
                if new_word is False:
                    file.write(mdict[str(data[beginning:len(data) - 1])])
        except IOError:
            print(f'Cannot open output file: {name_of_file}.txt')
            exit(1)
    else:
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                data = file.read()
        except IOError:
            print(f'Cannot open input file: {filename}')
            exit(1)
        new_word = True
        beginning = 0
        for i in range(0, len(data)):
            if data[i] == '\\' or data[i] == '/':
                new_word = True
                print(' ', end='')
            elif data[i] == '\n':
                if new_word is False:
                    print(mdict[str(data[beginning:i])], end='')
                new_word = True
                print('')
            elif data[i] == '.' or data[i] == '-':
                if new_word:
                    beginning = i
                    new_word = False
            elif data[i] == ' ':
                if new_word is False:
                    new_word = True
                    print(mdict[str(data[beginning:i])], end='')
            else:
                raise ValueError(f'File contains {data[i]} at index: {i}. Cannot decode.')
        if new_word is False:
            print(mdict[str(data[beginning:len(data) - 1])], end='')


def decode_gui(morse_frame, txt_frame):
    mdict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
             '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
             '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
             '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
             '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-.-.-': '.', '--..--': ',',
             '..--..': '?'}
    txt_frame.delete(1.0, 'end')
    data = morse_frame.get(1.0, 'end')
    new_word = True
    beginning = 0
    try:
        for i in range(0, len(data)):
            if data[i] == '\\' or data[i] == '/':
                new_word = True
                txt_frame.insert('end', ' ')
            elif data[i] == '\n':
                if new_word is False:
                    txt_frame.insert('end', mdict[str(data[beginning:i])])
                new_word = True
                txt_frame.insert('end', '\n')
            elif data[i] == '.' or data[i] == '-':
                if new_word:
                    beginning = i
                    new_word = False
            elif data[i] == ' ':
                if new_word is False:
                    new_word = True
                    txt_frame.insert('end', mdict[str(data[beginning:i])])
        if new_word is False:
            txt_frame.insert('end', mdict[str(data[beginning:len(data) - 1])])
    except KeyError:
        txt_frame.insert('end', f'UNSUPPORTED SIGN AT INDEX {i}')
        return
