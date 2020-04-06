import sys

def setMenu(bur,bev):
    return bur+bev-50


burger = {'high':0, 'med':0, 'low':0}
beverage = {'coke':0, 'cider':0}
burgerName = ['high', 'med', 'low']
beverageName = ['coke', 'cider']
for key in burgerName:
    price = int(sys.stdin.readline())
    burger[key] = price
for key in beverageName:
    price = int(sys.stdin.readline())
    beverage[key] = price
print(setMenu(min(burger.values()),min(beverage.values())))