import re

str1 = 'paraparaparadise'
str2 = 'paragraph'

def bigram_str(sent):
    sent = re.compile('\.|\s').sub('', sent)
    strs = []
    for i,v in enumerate(sent):
        if i+1 <= len(sent)-1:
            strs.append(sent[i] + sent[i+1]) 
    return strs

if __name__ == "__main__":
    X = set(bigram_str(str1))
    Y = set(bigram_str(str2))

    # 和集合
    # print(X.union(Y))
    print(X|Y)    

    # 積集合（共通部分）
    # print(X.intersection(Y))
    print(X&Y)

    # 差集合
    # print(X.difference(Y))
    print(X-Y)

    # どちらか一方に属する要素
    # print(X.symmetric_difference(Y))

    # 'se'というbi-gramがXおよびYに含まれているかどうか
    print('se' in (X&Y))
    
