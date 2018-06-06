#老人与海.py

def Deal() :
    txt = open("mansea.txt", "r").read()
    txt.lower()
    for ch in "!'(),.:;":
        txt = txt.replace(ch, " ")
    return txt

t = Deal()
words = t.split()
counts = {}
for word in words :
    counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10) :
    word,count = items[i]
    print(word, '--',count)
