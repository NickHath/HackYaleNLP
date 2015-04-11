# Natural Language Toolkit: code_document_classify_fd
# Natural Language Processing with Python, by Steven Bird, Ewan Klein, 
# and Edward Loper. O'Reilly Media, 978-0-596-51649-9.

import nltk
from nltk.corpus import movie_reviews
import random

# a list of:
# (['all', 'the', 'words', 'in', 'a', 'positive', 'review', 'file'], pos)
documents = [(list(movie_reviews.words(fileid)), category)
				for category in movie_reviews.categories()
				for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# {'all': count, 'words': count, 'in': count, 'corpus': count}
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# the features for this model are unigram counts of the 2000 most frequent words!
word_features = all_words.keys()[:2000] 

def document_features(document): 
	# vocabulary of the document
    document_words = set(document) 
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words) # returns a bool
    return features

# test on a sample review file
# print document_features(movie_reviews.words('pos/cv974_22941.txt'))

# [({'contains(word)': True, 'contains(other_word)': False}, 'pos'), ...]
f_sets = [(document_features(d), c) for (d,c) in documents]

# train on the last 1900 elements
# test on the first 100
# remember these are random (due to random.shuffle(documents))
train_set = f_sets[100:]
test_set = f_sets[:100]

# a classifier is an object in NLTK
classifier = nltk.NaiveBayesClassifier.train(train_set)

# test the model
print (nltk.classify.accuracy(classifier, test_set))

num_features = 10
classifier.show_most_informative_features(num_features)
