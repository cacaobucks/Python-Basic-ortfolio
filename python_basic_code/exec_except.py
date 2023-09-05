try:
    a = int(input("割られる数を入力してください："))
    b = int(input("割る数を入力してください："))
    c = a / b
    
    
except ZeroDivisionError:
    print("エラー：0で割り算しないでください")


except ValueError:
    print("エラー：数値を入力してください")

else:
    print(f"{a} ÷ {b} = {c}")


finally:
    print("処理を終了します")
