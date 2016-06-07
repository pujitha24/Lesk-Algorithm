__author__ = 'puji'
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


def main():
 sense=[]
 dict={}
 ps = PorterStemmer()
 s = "Time flies like an arrow"
 words = nltk.word_tokenize(s)
 words = [word for word in words if word not in stopwords.words('english')]
 max_overlap=0
 synonyms=[]
 for i in words:
  deflist=[]
  deflist2=[]
  max_overlap=0
  finalsy=""
  ind=words.index(i)
  synsets=wordnet.synsets(i)
  otherlist=words[:ind]+words[ind+1:]
  deflist2=contextwords(otherlist,dict)
  overlap1=[]
  for synset in synsets:
   deflist=getexamples(synset)
   d=stemstoplist(deflist)
   onlyinA=stemstoplist(deflist2)
   new=set(d)
   onlyinA1=set(onlyinA)
   overlap=[]
   overlap=list(new.intersection(onlyinA1))
   if (len(overlap))>= max_overlap:
        max_overlap=len(overlap)
        overlap1=overlap
        finalsy=synset
  print(overlap1)
  print(finalsy)
  print(max_overlap)
  dict[i]=finalsy
 print(dict)
def stemstoplist(deflist):
   ps = PorterStemmer()
   a1=set(deflist)
   b1=set(stopwords.words('english'))
   d=a1.difference(b1)
   d=[ps.stem(i) for i in d]
   return d
def getexamples(synset):
   deflist=[]
   deflist=word_tokenize(no_punct(synset.definition().lower()))
   deflist1=[]
   for example in synset.examples():
     example = no_punct(example)
     example=example.lower()
     deflist1.extend(word_tokenize(example))
   deflist.extend(deflist1)
   return deflist
def contextwords(otherlist,dict1):
    contextlist=[]
    for other in otherlist:
     if other in dict1:
      k=dict1[other]
      contextlist.extend(getexamples(k))
     else:
      for syn in wordnet.synsets(other):
          contextlist.extend(getexamples(syn))

    return contextlist
def no_punct(example):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct1 = ""
    for char in example:
      if char not in punctuations:
       no_punct1 = no_punct1 + char
    return no_punct1


if __name__=='__main__' :
    main()