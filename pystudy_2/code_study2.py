score = float(input(">100"))
if score == 5:
    print("졸려")
elif 4 < score:
    print("개졸려")
elif 3.5 <= score :
    print("완전 졸려")
if score == 5 and score - 1 == 4:
    print("자자 슈발")
if 2 <= 3:
    print("조 ㄴ 나 졸 려")

alist = [1,2,3,4,5]
print("이선민지각")
if 4 in alist:
    print("선민이 또 안왔니?")
if 121 not in alist:
    print("날라리 이선민")

    alist = alist + [1]
    alist = alist * 2
    alist.append(8)
    print("응애")
    print(alist + [2])
    print(alist * 3)
    for element in alist:
        print("go home")