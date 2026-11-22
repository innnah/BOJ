'''
Input consists of a number of lines, each representing a transaction. Each transaction 
consists of an integer representing the starting balance (between –200 and +10,000), 
the letter W or the letter D (Withdrawal or Deposit), followed by a second integer 
representing the amount to be withdrawn or deposited (between 5 and 400). Input will
be terminated by a line containing 0 W 0.

출력
Output consists of one line for each line of input showing the new balance for each 
valid transaction If a withdrawal would take the balance below -200, the output must 
be the words ‘Not allowed’.
'''

while 1:
    l = input().split()
    a, b, c = l
    a = int(a)
    c = int(c)
    if a == 0 and c == 0 and b == 'W': break
    if b == 'D':
        print(a+c)
    else:
        if a-c < -200:
            print("Not allowed")
        else:
            print(a-c)