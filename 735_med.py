asteroids = [10,2,-5]
arras = []
cnt = 0

for aster in asteroids:
    if aster < 0:
        arras.append(abs(aster))
    for aster2 in arras:
        if aster2 > aster:
            print(aster)

