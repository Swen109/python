life = {'animals': {
    'cats':[
        'Henri', 'Grumpy', 'Lucy'
        ], 
        'octopi': {}, 
        'emus': {}
        },
        'plants': {},
        'other': {}
}

# 7.印出life最頂端的鍵
print( list( life.keys() ) )

# 8.印出life['animals']的鍵
print( list( life['animals'].keys() ) )

#9.印出life['animals']['cats']的值
print( life['animals']['cats'] )