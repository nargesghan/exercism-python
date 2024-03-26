def abbreviate(words):
    acronym=''
    words=[word for part in words.split(' ') for word in part.split('-')]
    for word in words:
        word=word.strip('_!.')
        if len(word)!=0:
            acronym=acronym+word[0]
    acronym=acronym.upper()
    return acronym