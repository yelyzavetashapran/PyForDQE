a = """homEwork:

tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View.also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.

last iz TO calculate nuMber OF Whitespace characteRS in this Text.caREFULL, not only Spaces, but ALL whitespaces.I got 87."""
def one():
    output = ''
    last_words = []
    for i in a.lower().split('\n'):  # Convert string into lower case and split it by '\n'
        for y in i.split('.'):  # Split again by '.'
            if y.find('iz') != -1:  # If 'iz' not False

                y = y.replace(' iz ', ' is ')  # Replace 'iz' with 'is' add space for replacement only where it's needed

            last_word = [i.replace(':', '') for i in y.split(' ') if i != '' and len(
                y) > 0 and not i.isdigit()]  # Create lists with every word (but not number) of every sentence, including empty (when '/n')

            if len(last_word) > 0:  # If list not empty
                last_words.append(last_word[-1])  # Append last word from each sentence to list

            # Creating new punctuation marks
            if y == '':
                output += '\n'  # Add new '\n'
            elif y[-1].isalpha():
                output += y.capitalize() + '. '  # Add new '. ' to the end of every sentence
            elif y[-1].isdigit():
                output += y.capitalize() + '.'  # For sentence 'I got 87'
            elif y[-1] == ':':
                output += y.capitalize() + '\n'  # For sentence 'Homework'

        last_words_sentance: str = ' '.join(last_words) + '.'  # Create a new sentence(string) from list 'last_words'

    return output, last_words_sentance

output, last_words_sentance = one()

def two():
     whitespaces = output.count('\n') + output.count(' ')
     return whitespaces

def three():
     result = output[:output.find('paragraph.')+10] + '\n' + last_words_sentance.capitalize() + output[output.find('paragraph.')+10:]  # Final output
     return result

print(three())
print('Count of whitespaces:', two())
