# Natural Language Toolkit
# See: Natural Language Processing with Python, by Steven Bird, Ewan Klein, 
# and Edward Loper. O'Reilly Media, 978-0-596-51649-9.

import nltk
from nltk.corpus import names
import random

def features(word):
	return { 'last_letter' : word[-1] }

labeled_names = [(n, 'male') for n in names.words('male.txt')] 
labeled_names += [(n, 'female') for n in names.words('female.txt')]

random.shuffle(labeled_names)

f_sets = [(features(n), gender) for (n, gender) in labeled_names]
train_set = f_sets[500:]
test_set = f_sets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)

# what would our model choose for Karen?
#print classifier.classify(features('Karen'))

# print accuracy of classifier
print nltk.classify.accuracy(classifier, test_set)

# show the features that most predict male/female
print classifier.show_most_informative_features(10)
