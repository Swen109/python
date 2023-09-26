# 1.製作e2f字典
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}

# 2.印出walrus的法文單字
print(e2f["walrus"])

# 3.用e2f製作法英字典，稱之為f2e。使用item方法
e2f_list = list(e2f.items())
f2e = []
for i, j in e2f_list:
    f2e.append([j, i])
f2e = dict(f2e)

# 4.印出chien的英文
print(f2e["chien"])

# 5.印出e2f的英文單字集合
print(set(e2f.keys()))