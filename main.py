print("-- Write Text --\n-- <q: quit> --")
n = 1
storage = "" # default value
while (user_input := input(f"{n}: ")) != "q":
  # user_input은 계속 현재 값으로 초기화 됩니다
  n += 1
  storage += user_input + "\n"
