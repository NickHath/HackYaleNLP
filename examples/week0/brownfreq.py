from nltk.corpus import stopwords, brown
from nltk import FreqDist
from nltk.text import Text
import matplotlib

sw = stopwords.words('english')
old_brown = brown.words(categories='news')

new_brown = [w for w in old_brown if w.lower() not in sw
								  and w.isalnum()]

fdist = FreqDist(Text(new_brown))
fdist.plot(25, cumulative=False)
