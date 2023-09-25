#用串列生成式製作名叫even的串列，讓它擁有range(10)內的偶數
even = [i for i in range(10) if i % 2 == 0]
print(even)