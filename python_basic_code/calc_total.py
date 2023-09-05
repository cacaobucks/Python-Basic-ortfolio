score = int(input("税抜価格を入力してください："))
score1 = score + (score//10)
score2 = score + (score//10) + 350

if score >= 2000:
     print("送料はかかりません。")
     print("税込価格は", score1, "です。")

else:
    if score < 2000:
         print("送料として350円かかります。")
         print("送料込みの価格は", score2, "です。")
