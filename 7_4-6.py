#將人名改為字首大寫並印出
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()

#將乳酪改為字首大寫
things[0] = things[0].capitalize()

#將病元素去除
things.remove(things[2])
print(things)