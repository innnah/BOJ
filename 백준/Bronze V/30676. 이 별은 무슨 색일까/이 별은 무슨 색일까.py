'''
빨간색: 620nm 이상 780nm 이하
주황색: 590nm 이상 620nm 미만
노란색: 570nm 이상 590nm 미만
초록색: 495nm 이상 570nm 미만
파란색: 450nm 이상 495nm 미만
남색: 425nm 이상 450nm 미만
보라색: 380nm 이상 425nm 미만
입력
계기판에 표시된 별빛의 파장 
$\lambda$ 가 주어진다. 파장은 항상 정수로 주어지며 단위는 
$\textrm{nm}$이다. 
$(380 \leq \lambda \leq 780)$ 

출력
별의 색을 출력한다. 빨간색이면 "Red", 주황색이면 "Orange", 노란색이면 "Yellow", 
초록색이면 "Green", 파란색이면 "Blue", 남색이면 "Indigo", 보라색이면 "Violet"을 출력한다.
'''
k=int(input())
if 380 <= k < 425: print("Violet")
elif 425 <= k < 450: print("Indigo")
elif 450 <= k < 495: print("Blue")
elif 495 <= k < 570: print("Green")
elif 570 <= k < 590: print("Yellow")
elif 590 <= k < 620: print("Orange")
else: print("Red")