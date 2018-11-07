import textDeal
import AnswerSearch
import question

def singelquestion():
  str1 = input("Enter your text file path: ")
  str2 = input("Enter your question: ")
  q = question.Q(str2)
  sto = question.Q(str2).stock
  t = textDeal.T(str1)
  res = []
  if q.Qtype == "1":
    temp = AnswerSearch.answer1(sto,t)
  elif q.Qtype == "2":
    temp = AnswerSearch.answer2(sto, t)
  elif q.Qtype == "3":
    temp = AnswerSearch.answer3(sto, t)
  elif q.Qtype == "4":
    temp = AnswerSearch.answer4(sto, t)
  elif q.Qtype == "5":
    temp = AnswerSearch.answer5(sto, t)
  else:
    temp = []
    print("Please Enter correct type of question!")

  if temp:
    res.append(["A:" + temp[0][0], "Sourse:" + t.text[temp[0][-1]], "(line" + str(temp[0][-1]) + ")"])
  for i in range(1, len(temp)):
    if temp[i][0] != temp[i - 1][0]:
      res.append(["A:" + temp[i][0], "Sourse:" + t.text[temp[i][-1]], "(line" + str(temp[i][-1]) + ")"])

  if res:
    for i in res:
      for j in i:
        print(j)
  else:
    print ("No information available.")

def mutiquestion():
  str1 = input("Enter your text file path: ")
  str2 = input("Enter your question file path: ")
  t = textDeal.T(str1)
  answer = []
  i = 0
  for line in open(str2).readlines():
    print(line)
    q = question.Q(line)
    sto = question.Q(line).stock
    res = []
    if q.Qtype == "1":
      temp = AnswerSearch.answer1(sto, t)
    elif q.Qtype == "2":
      temp = AnswerSearch.answer2(sto, t)
    elif q.Qtype == "3":
      temp = AnswerSearch.answer3(sto, t)
    elif q.Qtype == "4":
      temp = AnswerSearch.answer4(sto, t)
    elif q.Qtype == "5":
      temp = AnswerSearch.answer5(sto, t)
    else:
      temp = []
      print("question type incorrect")

    if temp:
      res.append(["A: "+temp[0][0], "Sourse:"+t.text[temp[0][-1]], "(line"+str(temp[0][-1])+")"])
    for i in range(1, len(temp)):
      if temp[i][0] != temp[i - 1][0]:
        res.append(["A: "+temp[i][0], "Sourse:"+t.text[temp[i][-1]], "(line"+str(temp[i][-1])+")"])

    if res:
      for i in res:
        for j in i:
          print(j)
    else:
       print("No information available.")



s = input("If you have mutiple questions,input a. If you have single question, input b: ")
if s == 'a':
  mutiquestion()
if s == 'b':
  singelquestion()


"""
for each in res:
  print("A:"+each[0])
  print("Source:"+each[1])
  print("(line"+str(each[2])+")")
"""

