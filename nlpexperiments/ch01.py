from nltk.book import *
from nltk.corpus import stopwords
from nltk import PorterStemmer,ne_chunk,pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

ps = PorterStemmer()
#sample = ''.join([char +' ' for char in text1[100:200]])
#print sample
sample = word_tokenize(text1)
words = sample[100:200]
stop_words = set(stopwords.words("english"))
filtered_words = [w for w in words if  w not in stop_words]

stemmed_words = [ps.stem(w) for w in filtered_words]
lemmatized_words = [lemmatizer.lemmatize(w) for w in filtered_words]

tagged = [pos_tag(w) for w in stemmed_words]

tagged = [ne_chunk(w) for w in tagged]
print (stemmed_words)
print (lemmatized_words)
print(tagged)