from nltk.book import *
from nltk.collocations import *
from nltk import bigrams,collocations

#can any of the below lines with text1, text2,text3 and text 4
print text1
keywords_set1 = ["analyst","company","graphs","charts","bars","reports","video","ticker"]
keywords_set2 = ["people","ships","drinks","party"]
keywords_set3 = ["growth","massive","improvement","great"]

print text1.concordance(keywords_set1[0])

print text1.similar(keywords_set3[0])

print text1.common_contexts(keywords_set1[0:len(keywords_set1)-1])

print text1.dispersion_plot(keywords_set2[0:len(keywords_set2)-1])

#print text1.generate()

print len(text1) #vocabulary

print len(sorted(set(text1)))

def lexical_diversity():
    print len(sortet(set(text1)))/len(text1)  #lexical richness

print text1.count("very")

def percentage():
    print 100 * text1.count("very")/len(text1)


""" Output similar to below
Genre	Tokens	Types	Lexical diversity
skill and hobbies	82345	11935	0.145
humor	21695	5017	0.231
fiction: science	14470	3233	0.223
press: reportage	100554	14394	0.143
fiction: romance	70022	8452	0.121
religion	39399	6373	0.162"""


tokens = text1[100:200]
print tokens
vocab = set(sorted(tokens))
print sorted(tokens)
print len(vocab)

fdistext1 = FreqDist(text1)
print fdistext1.most_common(50)

print fdistext1['whale']

fdistext1.plot(50,cumulative="true")

V = set(text1)

long_words = [w for w in V if len(w)>15]

print sorted(long_words)

print sorted(w for w in V if len(w)>5 and fdistext1[w]>7)

print list(bigrams(tokens))

print text1.collocations() 

print [len(w) for w in V]

fdistlenwords = FreqDist(len(w) for w in V)

print fdistlenwords.most_common()

print fdistlenwords.max()

"""
fdist = FreqDist(samples)	create a frequency distribution containing the given samples
fdist[sample] += 1	increment the count for this sample
fdist['monstrous']	count of the number of times a given sample occurred
fdist.freq('monstrous')	frequency of a given sample
fdist.N()	total number of samples
fdist.most_common(n)	the n most common samples and their frequencies
for sample in fdist:	iterate over the samples
fdist.max()	sample with the greatest count
fdist.tabulate()	tabulate the frequency distribution
fdist.plot()	graphical plot of the frequency distribution
fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
fdist1 |= fdist2	update fdist1 with counts from fdist2
fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2
"""




