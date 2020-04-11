#파이썬 구구단 (gugudan.py )

print(f'오진희  ---  구구단 출력')
for i in range(1,10,1):

    print('*' * 30)
    print(f'{i} 단')
    print('*'*30)
    for j in range(1,10,1):
        print(f'{i} x {j} = {i*j}')
    print('\n')
print('*' * 50)

# 수정: 2020-04-10
# 수정: 2020-04-11