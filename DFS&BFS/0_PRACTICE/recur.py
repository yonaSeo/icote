def rec_func(i):
    if i == 5:
        print(f"{i}번째로 함수 호출 종료한다.")
        return
    print(f"{i}번째 함수가 {i+1}번째 함수를 호출한다.")
    rec_func(i + 1)
    print(f"{i}번째 함수 종료한다.")

rec_func(1)