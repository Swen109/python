# 用下列格式印出每一個問題以及它的答案
# Q: 問題
# A: 答案

questions = ['AAA', 'BBB', 'CCC']
answers = ['ccc','aaa' , 'bbb']

ans_c, ans_a, ans_b = answers
answers = [ans_a, ans_b, ans_b]

for i, j in zip(questions,answers):
    print(f'Q: {i}\nA: {j}\n')
    