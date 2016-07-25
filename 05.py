import sys
import re

def bigram_word(sent):
    sent = re.compile('\.').sub('', sent)
    token = sent.split(' ')
    words = []
    for i,v in enumerate(token):
        if i+1 <= len(token)-1:
            words.append([token[i] + ' ' + token[i+1]]) 
    return words
    
def bigram_str(sent):
    sent = re.compile('\.|\s').sub('', sent)
    strs = []
    for i,v in enumerate(sent):
        if i+1 <= len(sent)-1:
            strs.append([sent[i] + sent[i+1]]) 
    return strs

if __name__ == "__main__":
    default_str = 'I am an NLPer'
    if len(sys.argv) is not 1:
        param = sys.argv[1]
    else:
        param = default_str
    print('単語 bi-gram:')
    print(bigram_word(param))
    print('文字 bi-gram:')
    print(bigram_str(param))

