# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

# sed s/[[:cntrl:]]/\ /g hightemp.txt
cat './hightemp.txt' | tr '\t' '\ '
# expand -t 1 hightemp.txt

