# #점수판독기
# score = int(input('점수를 입력하세요'))

# if score >= 90: 
#     print('A')
# elif score >= 80: # 90>score>80을 할 필요가 없는게, elif를 적었기 때문에 위에서 1번 걸렀기 때문. else if 
#     print('B')
# elif score >= 70:
#     print('C')
# else:
#     print('넌 F')

#선택하고 ctrl+/ 하면 모두 주석 처리 됨.(위에 코드 작동 안되게 하는 법)


#==이 '같다면'이라는 뜻이고, = 는 변수를 정의할 때 주로 씀.

#3의 배수 판별기
num = int(input('3의 배수 판별기입니다. 숫자를 입력하세요.'))


if num % 3 == 0:
    print('3의 배수가 맞습니다.')
else:
    print('3의 배수가 아닙니다.')


num = int(input('5의 배수 판별기입니다. 숫자는?'))
cal = number%5

if cal == 0:
    print('5의 배수입니다.')

