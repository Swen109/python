# 使用zip() tuple('optimist', 'pessimist', 'troll'),
# tuple('The glass is half full.', 'The glass is half empty.', 'How did you get a glass?')
# 來製作一個字典

who = ('optimist', 'pessimist', 'troll')
says = ('The glass is half full.', 'The glass is half empty.', 'How did you get a glass?')

script = dict(zip(who, says))