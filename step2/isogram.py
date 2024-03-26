def is_isogram(string):
    string=string.lower()
    string = string.replace("-", "").replace(" ", "")
    word_dictionary={}
    for char in string:
        word_dictionary[char]=word_dictionary.setdefault(char,0)+1
        if word_dictionary[char]>1:
            return False
    return True
