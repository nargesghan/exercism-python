# def score(word):
#     score=0
#     word=word.lower()
#     values={1:'aeioulnrst',2:'dg',3:'bcmp',4:'fhvwy',5:'k',8:'jx',10:'qz'}
#     for char1 in word:
#         for key,string in values.items():
#             for char2 in string:
#                 if char1==char2:
#                     score+=key
#     return score
                    
        

    

#using maketrans:

def score(word):
    values = {'aeioulnrst': 1, 'dg': 2, 'bcmp': 3, 'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10}
    trans = {ch: str(val) for group, val in values.items() for ch in group}
    table = str.maketrans(trans)
    return sum(int(ch) for ch in word.lower().translate(table))

