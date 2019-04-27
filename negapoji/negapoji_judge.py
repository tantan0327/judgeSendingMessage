import sys
from negapoji import feeling

sentence = input("Please enter your sentence: ")
negapoji = feeling.feeling()

def isSentenceShort(str):
    if(len(str) <= 10):
        return True;

def getResult():
    if (isSentenceShort(sentence)):
        return "文章が短すぎます。"
    if not negapoji.judge(sentence):
        return "ネガティブな文章です。"
    else:
        return "ok"

print(getResult())
