def loadingBar(maximumNumber, currentNumber):
    p = (currentNumber/maximumNumber)*100
    load = '[{}] {}%'.format(('█'*(round(p/100*20))).ljust(20, '.'), str(round(p, 2)).ljust(5))
    print('\b'*len(load), end='', flush=True)
    print(load, end='')