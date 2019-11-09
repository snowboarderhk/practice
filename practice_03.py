"""
people = {"G. Bluth II": "A. Development",
          "Barney":"HIMYM","Dennis":"Always Sunny",}

for i in people:
  print(i)
"""

"""
tv = ["GOT","Narcos","Vice"]
i = 0
for show in tv:
    new =tv[i]
    new =new.upper()
    tv[i]= new
    i +=1
print(tv)

x = 10
while x > 0 :
    print('{}'.format(x))
    x -= 1
print("Happy new year!!")

for i in range(0,1000):
    print(i)
    if i ==10:
        break


qs = ["what is your name","what is your fav. color?",
        "what is your quest?"]

n=0
while True:
    print('Type q to quit')
    a = input(qs[n])
    if a == "q":
        break
    n = (n+1)%3

for i in range(1,6):
    if i ==3:
        continue
    print(i)

# p116 challenge
print("---No.1---")
test1 = ['Walking Dead',"Antrajue","The Sopranos","vanpair Diarease"]
for name in test1:
    print(name)

print("---No.2---")
for i in range(25,51):
    print(i)

print("---No.3---")
n=0
for name in test1:
    print("{}".format(n),name)
    n+=1
print("---No.4---")
coll = ["1","3","4","5"]
while True:
    ans = input("Type your answer")
    flag = 0
    for a in coll:
        if ans == a:
            flag = 1
            print("a=",a)
            print("flag",flag)
            print("ans=",ans)
            print("----")
    if flag ==1:
        print("collect!!")
    else:
        print("Wrogn@@@")
    if ans == "q":
        break
    flag =0
print("----No.5---")
list1 = [8,19,148,4]
list2 = [9,1,33,83]
list_ans = []
for i in list1:
    for j in list2:
        list_ans.append(i*j)
print(list_ans)
"""
#+++++++++++++++++++++++++
"""
import math
math.pow(2,4)
print(math.pow(2,4))

import random
import statistics
import keyword

#Data =[]
#for i in range(0,1000):
#    Data.append(random.randint(0,100))
#mean = statistics.mean(Data)
#median = statistics.median(Data)
#mode = statistics.mode(Data)
#print(mean,median,mode)

print(keyword.iskeyword("and"))
print(keyword.iskeyword("for"))
print(keyword.iskeyword("data"))


import sayhelloworld as shw
shw.print_hello(10)
"""
#=========p123=======no.1========
"""
import statistics as st
import random
numberList = []
for i in range(1000):
    numberList.append(random.randint(0,1000))
average = st.mean(numberList)
print(average,average2)

#No.2
import p123_no2
print(p123_no2.pow3(9.3))
"""
"""
import os
path = os.path.join("Users","hirokazukajima","デスクトップ","Python")

st = open("output/st.txt","w")
st.write("Hi from python.日本語は")
st.close()

a = [1,2,3,4,5]
b = []

with open("./output/st2.txt","w") as f:
    f.write("Hi from python.日本語は")

with open("./output/st2.txt","r") as f:
    #print(f.read())
    b.append(f.read())
print(b)

import csv

with open ("./output/st3.csv","w",newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow([1,2,3])
    w.writerow([4,5,6])

with open("./output/st3.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))


"""

#3===p132 challenge 2===
"""
answer = input("where is your best place?")
with open("./output/challenge2.txt","w") as f:
    f.write(answer)
"""
"""
#===p132 challenge 3===
import csv
base = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],
        ["Training Day","Man on Fire","Flight"]]
base2 =[]
for i in base:
    base2.extend(i)
with open("./output/challenge3.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(base2)

#===解答例===
import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
"""
