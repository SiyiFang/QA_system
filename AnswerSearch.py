import textDeal
import NameSybol
import re

def NormalStockName(stock):
    stock= stock[0].capitalize()+stock[1:]
    s,n,names  = [],[stock]+stock.split(' '),[]
    if stock in NameSybol.stockSymbol:
        s.append(stock)
        n.append(NameSybol.stockName[NameSybol.stockSymbol.index(stock)])
    elif stock in  NameSybol.indeSymbol:
        s.append(stock)
        n.append(NameSybol.indeName[NameSybol.indeSymbol.index(stock)])

    for k in range(len(NameSybol.stockName)):
        if stock.lower() in NameSybol.stockName[k].lower() or NameSybol.stockName[k].lower() in stock.lower():
            s.append(NameSybol.stockSymbol[k])
            names.append(NameSybol.stockName[k])
    for k in range(len(NameSybol.indeName)):
        if stock in NameSybol.indeName[k].lower() or NameSybol.indeName[k].lower() in stock.lower():
            s.append(NameSybol.indeSymbol[k])
            names.append(NameSybol.indeName[k])

    n = list(set(n))
    if "the" in n:
        n.pop(n.index('the'))
    if "The" in n:
        n.pop(n.index('The'))
    if "Inc" in n:
        n.pop(n.index('Inc'))
    if "inc" in n:
        n.pop(n.index('inc'))
    names = [list(set(s)),n]
    return names

#return list, each is [stock,setence,setenceNum]
def stockSentence(stock,t):
    names = NormalStockName(stock)
    nameMatch = []
    for i in range(len(t.textInfo)):
        for n in names[0]:
            if n in t.textInfo[i]:
                nameMatch.append([n,t.textInfo[i],i])
    for i in range(len(t.textInfo)):
        for n in names[1]:
            if n.lower() in t.textInfo[i].lower():
                nameMatch.append([n, t.textInfo[i], i])
    return nameMatch

# type(t) : Text
def answer1(stock,t):
    answer = []
    M = stockSentence(stock,t)
    for each in M:
        h1 = re.compile(r'.*\b(?i)(%s)\b.*\bfall\b' % each[0])
        h2 = re.compile(r'.*\b(?i)(%s)\b.*\b n\'t fall\b' % each[0]) #no up or lower
        h3 = re.compile(r'.*\b(?i)(%s)\b.*\brise\b' % each[0])
        h4 = re.compile(r'.*\b(?i)(%s)\b.*\b n\'t rise\b' % each[0])
        if h2.match(each[1]):
            answer.append(['It rose',each[0],each[1],each[2]])
        elif h1.match(each[1]):
            answer.append(['It fell', each[0], each[1], each[2]])
        if h4.match(each[1]):
            answer.append(['It fell', each[0], each[1], each[2]])
        elif h3.match(each[1]):
            answer.append(['It rose', each[0], each[1], each[2]])

    return answer

# type(t) : Text
def answer2(stock,t):
    answer = []
    M = stockSentence(stock, t)
    for each in M:
      h1 = re.compile(r'.*\b(?i)(%s)\b.*?\bfall\s(\w+\s)?(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
      h2 = re.compile(r'.*\b(?i)(%s)\b.*?\bfall\s(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
      if h2.search(each[1]):
        answer.append([h2.search(each[1]).group("num"), each[0], each[1], each[2]])
      elif h1.search(each[1]):
        answer.append([h1.search(each[1]).group("num"), each[0], each[1], each[2]])
    return answer

def answer3(stock,t):
    answer = []
    M = stockSentence(stock, t)
    for each in M:
      h1 = re.compile(r'.*\b(?i)(%s)\b.*\brise\s(\w+\s)?(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
      h2 = re.compile(r'.*\b(?i)(%s)\b.*?\brise\s(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
      if h2.search(each[1]):
          answer.append([h2.search(each[1]).group("num"), each[0], each[1], each[2]])
      elif h1.search(each[1]):
          answer.append([h1.search(each[1]).group("num"), each[0], each[1], each[2]])
    return answer

def answer4(stock,t):
    answer = []
    M = stockSentence(stock, t)
    for each in M:
        h1 = re.compile(r'.*\b(?i)(%s)\b.*\bclose\s(\w+\s)?(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
        h2 = re.compile(r'.*\b(?i)(%s)\b.*?\bclose at\s(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
        h3 = re.compile(r'.*\b(?i)(%s)\b.*?\bclose\s(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
        if h2.search(each[1]):
            answer.append([h2.search(each[1]).group("num"), each[0], each[1], each[2]])
        elif h3.search(each[1]):
            answer.append([h3.search(each[1]).group("num"), each[0], each[1], each[2]])
        elif h1.search(each[1]):
            answer.append([h1.search(each[1]).group("num"), each[0], each[1], each[2]])

    return answer

def answer5(stock,t):
    answer = []
    M = stockSentence(stock, t)
    for each in M:
        h1 = re.compile(r'.*\b(?i)(%s)\b.*\bopen\s(\w+\s)?(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
        h2 = re.compile(r'.*\b(?i)(%s)\b.*?\bopen at\s(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
        h3 = re.compile(r'.*\b(?i)(%s)\b.*?\bopen\s(?P<num>(((\d+\s)(\d*\/\d*)?)|(\d+\.\d+)|(\d+)))' % each[0])
        if h2.search(each[1]):
            answer.append([h2.search(each[1]).group("num"), each[0], each[1], each[2]])
        elif h3.search(each[1]):
            answer.append([h3.search(each[1]).group("num"), each[0], each[1], each[2]])
        elif h1.search(each[1]):
            answer.append([h1.search(each[1]).group("num"), each[0], each[1], each[2]])

    return answer


