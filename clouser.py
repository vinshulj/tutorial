def outfun():
    def ininfunc(person,coins):
        coin=coins
        def infun():
            nonlocal coin
            coin -= 1
            if coin>1:
                print(f"{person} has {coin} coins left")
            elif coin==1:
                print(f"{person} has only {coin} coin")
            else:
                print(f"{person} is out of coin")
        return infun 
    return ininfunc
harry=outfun()
# gita=outfun("gita",6)
harry=harry("harry",4)

harry()
# print(dir(outfun))

def outfunc():
    coin=10
    def sub():
        nonlocal coin
        coin -=1
        print(coin)
    return sub
vin=outfunc()
vin()
vin()