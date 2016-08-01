'''08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．'''

def cipher(text):
    enc = ''
    for s in text:
        if ord(s) >= 97 and ord(s) <= 122:
            str = chr(219 - ord(s)) 
        else:
            str = s
        enc += str
    return enc

sent = "Now I need a drink, alcoholic of course, あいうえおかきくけこ after the heavy lectures involving quantum mechanics."
print(cipher(sent))

