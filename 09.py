''' 09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．'''

import random

def typoglycemia(sent):
    token = sent.split(' ')
    result = []
    for word in token:
        strs = [s for s in word]
        if len(strs) > 3:
            first_str = strs.pop(0)
            last_str = strs.pop()
            random.shuffle(strs)
            strs.insert(0, first_str)
            strs.append(last_str)
        shuffled_word = ''
        for s in strs:
            shuffled_word += s
        result.append(shuffled_word)
    return ' '.join(result)

sent = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# print(sent)
print(typoglycemia(sent))

