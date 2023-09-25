#將最後一個元素改為小寫 把它反過來 再將第一個字改為大寫
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise)