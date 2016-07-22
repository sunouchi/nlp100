import re

sent = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
sent = re.compile('\.').sub('', sent.lower())
token = sent.split(' ')
# print(token)

single_letters = [1, 5, 6, 7, 8, 9, 15, 16, 19]
for i, v in enumerate(token):
    if (i+1) in single_letters:
        symbol = token[i][0]
        num = 0
    else:
        symbol = token[i][:2]
        num = 1
    # dict.update({token[i], num})
    print({symbol.capitalize(), num})

