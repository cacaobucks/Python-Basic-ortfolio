def fib_funct(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_funct(n-1) + fib_funct(n-2)
 
a = int(input("何番目の数値を求めますか?:") )

print(fib_funct(a))
      
