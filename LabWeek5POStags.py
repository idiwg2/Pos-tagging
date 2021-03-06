
# coding: utf-8

# In[1]:

import nltk


# In[3]:

# POS Tagged Corpora:  Brown and Penn Treebank
# the Brown corpus has its own set of POS tags
from nltk.corpus import brown
# the tagged_sents function gives POS tagged sentences and tagged_words gives POS tagged words
print(brown.tagged_sents()[:2], '\n')
print(brown.tagged_words()[:50])


# In[4]:

# Each tagged word is a pair, which Python calls a tuple  
#  it behaves like a list except that you can't change the elements (immutable)
wordtag = brown.tagged_words()[0]
print(wordtag)
print(type(wordtag))
print(wordtag[0])
print(wordtag[1])


# In[6]:

# the brown corpus can also be accessed by category
print(brown.categories(), '\n')
brown_humor_tagged = brown.tagged_words(categories='humor', tagset='universal')
print(brown_humor_tagged[:50])


# In[8]:

# the chat corpus uses Penn POS tags
print(nltk.corpus.nps_chat.tagged_words()[:50])


# In[9]:

# Penn treebank
from nltk.corpus import treebank


# In[11]:

# use corpus methods to get the text as strings and as tokens as before
treebank_text = treebank.raw()
print(treebank_text[:50], '\n')
treebank_tokens = treebank.words()
print(treebank_tokens[:20])


# In[12]:

# but we also have functions to get words with tags and sentences with tagged words
treebank_tagged_words = treebank.tagged_words()
print(treebank_tagged_words[:50])


# In[13]:

treebank_tagged = treebank.tagged_sents()
print(treebank_tagged[:2])


# In[15]:

# Frequency distribution of tags in Penn Treebank
tag_fd = nltk.FreqDist(tag for (word, tag) in treebank_tagged_words)
print(tag_fd.keys(), '\n')
for tag,freq in tag_fd.most_common():
    print (tag, freq)


# In[17]:

# use the first letter of the POS tag to get classes of tags
tag_classes_fd = nltk.FreqDist(tag[0] for (word, tag) in treebank_tagged_words)
print(tag_classes_fd.keys(), '\n')
for tag,freq in tag_classes_fd.most_common():
    print (tag, freq)


# In[18]:

## POS Tagging

# Separating the data into training and test data
size = int(len(treebank_tagged) * 0.9)
treebank_train = treebank_tagged[:size]
treebank_test = treebank_tagged[size:]


# In[19]:

# Default Tagger assign 'NN' to every word
# creates the tagger
t0 = nltk.DefaultTagger('NN')
# show the effect of the tagger by tagging the first 50 words
print(t0.tag(treebank_tokens[:50]))


# In[21]:

# evaluate function applies the tagger t0 to the untagged version of treebank
#   and compares with the tagged version
print(t0.evaluate(treebank_test))


# In[22]:

# Unigram tagger learns tag with the highest probability for each word
# creates the tagger on the training set
t1 = nltk.UnigramTagger(treebank_train)
# show the effect of the tagger by tagging the first 50 words
print(t1.tag(treebank_tokens[:50]))
# evaluates the tagger on the test set
print(t1.evaluate(treebank_test))


# In[23]:

# Bigram Tagging with Backoff to Combine Taggers
# create a sequence of taggers with backoff to get a bigram tagger
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(treebank_train, backoff=t0)
t2 = nltk.BigramTagger(treebank_train, backoff=t1)
# Accuracy with BigramTagger: 
print(t2.evaluate(treebank_test))


# In[24]:

# Using the bigram tagger on some new text
text = "Three Calgarians have found a rather unusual way of leaving snow and ice behind. They set off this week on foot and by camels on a grueling trek across the burning Arabian desert."


# In[25]:

# But we should separate the text into sentences first
textsplit = nltk.sent_tokenize(text)
print(textsplit)


# In[26]:

# apply the word tokenizer to each sentence
tokentext = [nltk.word_tokenize(sent) for sent in textsplit]
print(tokentext)


# In[27]:

# use the t2 bigram tagger to tag each sentence tokens
taggedtext = [t2.tag(tokens) for tokens in tokentext]
print(taggedtext)


# In[28]:

# use the Stanford POS tagger to tag each sentence tokens
taggedtextStanford = [nltk.pos_tag(tokens) for tokens in tokentext]
print(taggedtextStanford)


# In[30]:

# show how to flatten a list of tagged tokens
taggedtext_flat = [pair for sent in taggedtext for pair in sent]
print(taggedtext_flat)
taggedtextStanford_flat = [pair for sent in taggedtextStanford for pair in sent]
print(taggedtextStanford_flat)


# In[ ]:



