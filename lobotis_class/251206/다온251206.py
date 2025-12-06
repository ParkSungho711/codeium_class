name = '고다온'
eat = '햄버거'
eat = '유산균'
if eat == '햄버거' and name == '고다온':
    print ('햄벅하다')
elif name == '고다온' and eat == '유산균':
    print('똥싸기')
else:
    print('배고프다')

eat = ['햄버거','유산균','스테이크','찰떡파이']
print(eat[1])

for i in eat:
    # print(i)
    if i == '햄버거':
        print('햄벅하다')
    elif i == '유산균':
        print('똥나온다')
    elif i == '스테이크':
        print('배불러서 못먹는다')
    elif i == '찰떡파이':
        print('살찐다')
    else:
        maybe = input('내가 먹고싶은것은 사실 : ')
        # print(maybe + '입니다')
        print(f'{maybe}입니다')

robot = 'robotis_nowon'
print(len(robot))
print(robot[6])