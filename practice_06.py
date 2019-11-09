
#import re
#text = """
#キリンは大昔から__複数名詞__ の興味の対象でした。キリンは__複数名詞__のなかで一番背が高いのですが、科学者たちはそのような長い
#__体の一部__をどうやって獲得したのか説明できんません。キリンの身長は__数値__　__単位__近くあり、その高さのほとんどは足と
#__体の一部__によるものです。
#"""
"""
def mad_libs(mls):
    hints = re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力：".format(word)
            new = input(q)
            mls = mls.replace(word,new,1)
        print("\n")
        mls = mls.replace("\n","")
        print(mls)
    else:
        print("error")

mad_libs(text)

"""

#+++++++++p215 challenge 3 ----
"""
import re
test = re.findall(".oo","The ghost that says boo haunts the loo")
print(test)
"""

from flask import Flask
app = Flask(__name__)


@app.route("/")

def index():
    return "hello world"

app.run(port = 8000)
