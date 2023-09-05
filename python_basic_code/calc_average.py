score_list = []
while True:
    score = int(input("点数を入力してください："))   
    if score == -1:
        break
    score_list.append(score)
 
s = sum(score_list)
n = len(score_list)
avg = s / n
    
print(n,"人の平均点は",avg,"です。")
