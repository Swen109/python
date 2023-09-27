#用集合生成式合range(10)之類的奇數來製作odd集合

odd = {num for num in range(10) if num % 2 == 1}
print(odd)