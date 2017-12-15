from nltk.corpus import reuters
from nltk import sent_tokenize,word_tokenize
from gensim.models import TfidfModel,LsiModel
from gensim.corpora import Dictionary
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
 
stop_words = stopwords.words('english') + list(punctuation)
 
def tokenize(text):
    words = word_tokenize(text)
    words = [w.lower() for w in words]
    return [w for w in words if w not in stop_words and not w.isdigit()]


# corpus  = []
docs = reuters.fileids()[0:4]

topics = []


# for item in docs:
#     corpus.append(list(word_tokenize(reuters.raw(item))))

# print(corpus[3])

# tfidf = TfidfModel(corpus)
# print(tfidf[doc[0]])
#tfidf.save('/tmp/foo.tfidf_model')


documents = [tokenize(reuters.raw(docs[0]))] #for file_id in docs[0]]
dictionary = Dictionary(documents)
#for item in docs[0]:
topics.append(reuters.categories(docs[0]))
corpus = [dictionary.doc2bow(d) for d in documents]
tfidf_model = TfidfModel(corpus, id2word=dictionary)
tfidf_values = tfidf_model[corpus]
#dict(tfidf_model[dictionary.doc2bow(tokenize(reuters.raw(docs[0])))])
# print tfidf_values[dictionary.token2id['year']]                     # 0.0367516096888
# print tfidf_values[dictionary.token2id['following']]                # 0.0538505795815
# print tfidf_values[dictionary.token2id['provided']]                 # 0.0683210467787
# print tfidf_values[dictionary.token2id['structural']]               # 0.0945807226371
# print tfidf_values[dictionary.token2id['japanese']]                 # 0.107960637598
# print tfidf_values[dictionary.token2id['downtrend']]                # 0.122670341446
#print(documents[2])
#print(corpus[2])

lsi = LsiModel(tfidf_values, num_topics=len(topics))
print(lsi[tfidf_values]) # project some document into LSI space