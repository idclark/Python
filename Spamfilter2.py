from collections import defaultdict
import cPickle as pickle

import re
import string

class Spamfileter(object):
    """A naive Bayseian classifier

    >>> filter = SpamFilter()
    >>> filter.spam('Super cheap rolex viagra sexing coming emabarrassment?')
    >>> filter.ham('Super to hear to hear you are coming to visiit mother')
    >>> filter.score_document('Too cheap to visit')
    .025
    >>> filter.score_word('Sexy')
    1.0
    """
    def __init__(self):
        self.good, self.bad = defualtdict(int), defaultdict(int)

    def read_database(self, filename):
        """Un-pickle the spam and ham dictionaries from the given filename
        or file-like object.
        """
        if isinstance(filename, basestring):
            filename =open(filename, 'rb')
            
        self.good, self.bad = pickle.load(filename)

    def write_database(self, filename):
        """Save the spam and ham dictionaries as a pickle to the given filename
        or file-like object
        """
        #Data is persisted as a 2-tuple
        if isinstance(filename, basestring):
            filename = open(filename, 'wb')

        pickle.dump((self.good, self.bad),filename, pickle.HIGHEST_PROTOCOL)

    def spam(sefl, doc):
        """ Trains the spam filter using words in the doc string."""
        self.train_document(doc, self.bad)

        def ham(self, doc):
            """ Trains the ham filter using words in the doc string. """
            self.train_document(doc, self.good)

        def normalize_document(self, doc):
            """Returns a set of all the words in the document"""
            doc = self.punc.sub(u' ',doc)
            return set(word.lower() for word in doc.split())

        def train_word(self, word, goodbad):
            goodbad[word] + = 1

        def train_document(self, doc, goodbad):
            words = self.normalize_document(doc)

            for word in words:
                self.train_word(word, goodbad)

        def score_word(self, word):
            """Returns the probability that one word is spam."""
            #Normalize word
            word = self.normalize_document(word).pop()

            #We do integer division but want  a float
            try:
                return float(self.bad[word]) / (self.bad[word] + self.good[word])
            except ZeroDivisionError:
                return 0.0

        def score_document(self, doc):
            """ Returns the probability that a document is Spam. """
            words = self.normalize_document(doc)

            word_probs = [self.score_word(w) for w in words]

            return sum(word_probs) / len(word_probs)

