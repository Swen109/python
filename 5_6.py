#根據調查大家喜歡用這種格式來命名：Boaty McBoatface, Horsey McHorseface, Trainy McTrainface
#使用格式化來為國家博覽會的優勝者 duck, gourd, spitz 印出名字

names = ['Duck', 'Gourd', 'Spitz']

for i in names:
    print('%sy Mc%sface' %(i,i))
    
for i in names:
    print('{name}y Mc{name}face'.format(name = i))
    
for i in names:
    print(f'{i}y Mc{i}face')