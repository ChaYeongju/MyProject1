## 함수 선언부 (매서드)
def add_func(n1,n2) :
    res = n1+n2
    return res

def sub_func(n1,n2) :
    return n1-n2


## 전역변수부(필드, 속성)
num1, num2, result = 100, 200, 0





## 메인 코드부 : main() 매서드
result = add_func(num1,num2)
print(num1, '+', num2,'=', result)


result = sub_func(num1,num2)
print(num1, '-', num2,'=', result)
