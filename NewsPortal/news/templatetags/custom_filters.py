from django import template

register = template.Library()
punctuation_list = ['.', ',', ';', ':', '"', "'", '\n', '/', '?', '!', '-', '#', '(', ')', '%', '^', '~', '`',
    '[', ']', '{', '}', '|', '<', '>', '&', '№', '@',
]

@register.filter()
def censor(text):
    bad_words = ['murder', 'kill', 'murderer', 'killer', 'killed', 'violence', 'cruelty',]
    str_word = text

    if not isinstance(text, str):
        raise TypeError(f'{type(text)} is not "str"')

    for x in punctuation_list:
        str_word = str_word.replace(x, ' ')
    str_word = str_word.split()
    for word in str_word:
        if word.lower() in bad_words:
            text = text.replace(word, f'{word[0]}{"*"*(len(word)-1)}')
    return text