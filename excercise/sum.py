def t(n):
    if n>10:
        return 0
    else:
        return n+t(n+1)

sum=t(0);
print(f"sum is : {sum}")
