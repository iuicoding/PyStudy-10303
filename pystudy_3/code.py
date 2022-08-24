def print_3_times():
    print("안녕하세요")
    print("안녕")
    print('ㅎㅇ')

print_3_times()


def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 3)

def print_n_time_var(n, *value):
    for i in range(n):
        for val in calue:
            print(val)



print_n_time_var(3, "이선민과 박시후", "돼지", "킹콩")