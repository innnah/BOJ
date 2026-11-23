for i in range(2, 101):
    for j in range(2, i+1):
        for k in range(j, i+1):
            for l in range(k, i+1):
                if i**3 == j**3+k**3+l**3:
                    print(f"Cube = {i}, Triple = ({j},{k},{l})")