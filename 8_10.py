#用字典生成式來製作字典squares。使用range(10)來回傳鍵，並將各個鍵的平方當成它的值。
squares = {num: num*num for num in range(10)}
print(squares)