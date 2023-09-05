#九九のリストを作成する
list_add = []

for x in range(1,10):
    list_inner = []
    
    for y in range(1,10):
        list_inner.append(x*y)
        
        
    list_add.append(list_inner)
 
    
# 九九の表を表示する

for list_3d in list_add:
    for number in list_3d:
        print(f"{number:3}", end="")

    print("")
