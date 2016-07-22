import re
sent = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sent = re.compile('\.').sub('', sent.lower())
token = sent.split(' ')
print(sorted(token))
