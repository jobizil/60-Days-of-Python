from translate import Translator
# Exercise:
#  Write a program that translates from English to other language.
#  The program should take a file as input and output a file with the translated text.

# 1. Read the file
# 2. Translate the text
# 3. Write the translated text to a new file

try:
    with open('test.md', 'r') as file:
        read_file = file.read()
        translator = Translator(to_lang="es")
        translation = translator.translate(read_file)
        with open('translated.md', 'w') as my_file:
            my_file.write(translation)

except FileNotFoundError as error:
    print('File not found!')
