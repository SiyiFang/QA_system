from nltk import *
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(sentence):
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))
    return res



class T():
    def __init__(self,filepath):
        self.textInfo = []
        self.text = []
        self.path = filepath

        for line in open(self.path).readlines():
                self.text.append(line)
                f = re.compile('(low|slip|fell|shed|drop|decline|dip|crumble|down|plunge|plung|tumble|retreat|bearish|lose ground|dive|nosedive|crush|collapse|head south)')
                temp1 = f.sub('fall',' '.join(lemmatize_sentence(line.lower())))
                r =  re.compile('rise|climb|gain|up|advance|surge|jump|rebound|soar|rally|buoy|bullish|outperform|increase|bull|resume|upward|skyrocket')

                temp2 = r.sub('rise',temp1)
                o = re.compile('start|begin').sub('open',temp2)
                c = re.compile('end|finish ').sub('close',o)
                no = re.compile('never|no|not|none|neither|instead of|anything but|far away from').sub("n't", c)

                self.textInfo.append(no)





