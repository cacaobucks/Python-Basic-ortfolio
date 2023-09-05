alphabet_code = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"),0)


words = []
while True:
    word = input("英単語を入力してください：")   
    if word == '':
        break
    words.append(word)
    

    for letter in list(word):        
        alphabet_code[letter] += 1
    
    
print("入力した単語:",sorted(words))


for letter, count in alphabet_code.items():
    
    if count >= 1:
        print(f"{letter}" ,"が", f"{count}" ,"個ありました。")
