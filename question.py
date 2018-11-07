import re
import textDeal

class Q():
    def __init__(self,q):
        self.Qtype = 0
        self.stock = '0'

        if q[0].isupper():
            q = (q[0].lower())+q[1:]
        question = ' '.join(textDeal.lemmatize_sentence(q))
        question = (question[0].upper()) + question[1:]
        f = re.compile('(low|slip|fell|shed|drop|decline|dip|crumble|down|plunge|plung|tumble|retreat|bearish|lose ground|dive|nosedive|crush|collapse|head south)')
        temp1 = f.sub('fall', question)
        r = re.compile('rise|climb|gain|up|advance|surge|jump|rebound|soar|rally|buoy|bullish|outperform|increase|bull|resume|upward|skyrocket')
        question = r.sub('rise', temp1)
        Qtype1 = re.compile(r'Do (?P<stock>.*) rise or fall?')
        Qtype2 = re.compile(r'How much do (?P<stock>.*) rise?')
        Qtype3 = re.compile(r'How much do (?P<stock>.*) fall?')
        Qtype4 = re.compile(r'How much do (?P<stock>.*) close at?')
        Qtype5 = re.compile(r'How much do (?P<stock>.*) open at?')

        if Qtype1.match(question):
            self.Qtype = '1'
            self.stock = Qtype1.match(question).group("stock")
        elif Qtype2.match(question):
            self.Qtype = '2'
            self.stock = Qtype2.match(question).group("stock")
        elif Qtype3.match(question):
            self.Qtype = '3'
            self.stock = Qtype3.match(question).group("stock")
        elif Qtype4.match(question):
            self.Qtype = '4'
            self.stock = Qtype4.match(question).group("stock")
        elif Qtype5.match(question):
            self.Qtype = '5'
            self.stock = Qtype5.match(question).group("stock")
        else:
            self.Qtype= "I don't understand"

