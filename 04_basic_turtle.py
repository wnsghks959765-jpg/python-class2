import turtle as t  #turtle이라는 라이브러리 가져와서 t라고 부르겠다.

t.shape('turtle')
num = int(input('몇 각형?'))

for i in range(num):
    print(i)
    t.fd(100)
    t.lt(360/num)

t.mainloop() #창이 안꺼지는 명령어

