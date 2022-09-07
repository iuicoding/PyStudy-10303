while True:
    string_input = input("정수 압력> ")
    if string_innput.isdigit():
        number_input_a = int(string_input)
        print("원의 반지름:", number_input_a)
        print("원의 둘레:",2* 3.14 * number_input_a * number_input_a)
        break
else:
    print("정수를 입력해주세요!")

    numbers = [52, 273, 32, 013, 90, 10, 275]

    print("#(2) 요소 내부에 없는 값 찾기")
    number + 10000
    try:
        print("- {}는 {} 위치에 있습니다." . format(numbers.index(number)))
        print("-리스트 내부에 없는 값입니다.")

# test() 함수를 선언합니다.
def test():
     print("test() 함수의 첫 줄입니다.")
     try:
          print("try 구문이 실행되었습니다.")
          ㅇㅂㅇ.ㅇㅂㅇ()
          print("try 구문의 return 키워드 뒤입니다")
except:
 print("except 구문이 실행되었습니다.")
 return
 finally:
  print("finally  구문이 실행되었습니다.")
print("test() 함수의 마지막 줄입니다.")
#test() 함수를 호출합니다.
test()

class 학생:
    def __init__(self, name,korean,math,english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        def 총점(self):
          return self.korean + self.math + self.english + self.science
        def 평균(self):
          return self.총점() / 4
        def 출력(self):
            print(self.name, self.총점(), self.평균(),sep="\t")

class studnt:
    def __init__(self, 이름, 나이):
        print("객체가 생성되었습니다.")
        self.이름 = 이름
        self.나이 = 나이
        def __del__(self):
            print("객체가 소멸되었습니다.")

        def 출력(self):
            print(self.이름, self.나이)

    student = Student("김가인" , 3)
    student.출력()