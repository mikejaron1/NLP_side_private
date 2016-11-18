import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
# nltk.download()
stopwords = nltk.corpus.stopwords.words('english')
# print stopwords[:]
# print len(stopwords), "total stopwords"
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
