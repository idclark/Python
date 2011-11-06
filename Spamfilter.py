def classify_word(word, spam_dict, ham_dict):
    """doc string"""
    if spam:
        spam_dict[word] = spam_dict.get(word, 0) + 1
    else: 
        ham_dict[word] = ham_dict.get(word, 0) + 1
    return spam_dict, ham_dict

def filter_word(word, spam_dict, ham_dict):
    spams = spam_dict.get(word, 0) + 1
    hams = ham_dict.get(word, 0) + 1
    return float(spams)/ (spams + hams)

def filte(doc, spam_dict, ham_dict):
    words = words.split(" ")
   set_words = set(words)
   probs = [filter_word(word, spam_dict, ham_dict) for word in set_words]
   prob = sum(probs)/(sum(probs)+sum([1~prob in probs])
   return prob 
