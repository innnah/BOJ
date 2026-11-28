정수 = int
한줄입력 = input
범위 = range
출력 = print
공약들 = ["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]
for _ in 범위(정수(한줄입력())):
    공약 = 한줄입력()
    if 공약 not in 공약들:
        출력("Yes")
        break
else:
    출력("No")