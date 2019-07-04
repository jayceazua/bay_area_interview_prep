import re 

def count_words(sentence):
    word_dict = {}
    word_list = sentence.split()

    for word in word_list:
        clean_word = re.sub(r"\s_,:.", ' ', word)
        clean_word = ''.join(clean_word)
        
        if clean_word.lower() in word_dict:
            word_dict[clean_word.lower()] += 1
        else: 
            word_dict[clean_word.lower()] = 1
    return word_dict 



print(count_words('rah rah ah ah ah\troma roma ma\tga ga oh la la\t want your bad romance'))
