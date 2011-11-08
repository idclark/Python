def classify_word(word, spam,  spam_dict, ham_dict):
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

def filte_doc(words, spam_dict, ham_dict):
   words = doc.split(" ")
   set_words = set(words)
   probs = [filter_word(word, spam_dict, ham_dict) for word in set_words]
   prob = sum(probs)/(sum(probs)+sum([1-p for p in probs]))
   return prob 

def classify_doc(doc,spam, spam_dict={}, ham_dict={}):
    words = doc.split(" ")
    words = [word for word in words if word]
    set_words = set(words)
    for word in set_words:
        spam_dict, ham_dict = classify_word(word, spam, spam_dict, ham_dict)
    return spam_dict, ham_dict

                  
                    

