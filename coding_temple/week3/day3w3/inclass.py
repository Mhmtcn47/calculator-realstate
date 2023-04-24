# DESCRIPTION:
# Given a string, return a string that :
# Moves the first letter of each word to the end of it, then adds “ay” to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it(‘Pig latin is cool’) : ‘igPay atinlay siay oolcay’
# pig_it(‘Hello world !’)     : ‘elloHay orldway !’


# need to move the first letter of the word to the end of it
# then add "ay" to the end
# we need to append the modified word to the pig_words
# check the word if the world is alpha .isalpha()
def pig_it(str):
    words = str.split()
    pig_words = []
    # print(words)
    for word in words:
        if word.isalpha():
            pig_words.append(word[1:] + word[0] + "ay")
        else:
            pig_words.append(word)
    return(" ".join(pig_words))
print(pig_it("Pig latin is cool"))
print(pig_it("hello world !"))

# extra solution by dylan
# ap and lambda
def convert_to_pig_latin(astring):
    return ' '.join(map(lambda word: f'{word[1:]}{word[0]}ay' if word.isalpha() else word, astring.split()))

def convert_to_pig_latin_readable(astring):
    string_list = astring.split()
    for i, word in enumerate(string_list):
        if word.isalpha():
          word_to_pig_latin = f'{word[1:]}{word[0]}ay'
          string_list[i] = word_to_pig_latin
    return ' '.join(string_list)

def convert_to_pig_latin_list_comp(astring):
  return ' '.join(f"{word[1:]}{word[0]}ay" if word.isalpha() else word for word in astring.split())