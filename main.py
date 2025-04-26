print(">>> wt <<<")
n = 1
storage = "" # default value
while (user_input := input()) != "q":
  # user_input은 계속 현재 값으로 초기화 됩니다
  n += 1
  storage += user_input + "\n"
print(">>> quit <<<")
