import sys
import itertools

def divTeam(n):
    def calAbility(team):
        ability = 0
        members = itertools.combinations(team, 2)
        for member in members:
            ability += abilityMatrix[member[0]][member[1]] + abilityMatrix[member[1]][member[0]]
        return ability

    def checkAbility(start, link):
        startAbility = calAbility(start)
        linkAbility = calAbility(link)
        return abs(startAbility - linkAbility)

    count = n // 2
    members = range(n)
    starts = itertools.combinations(members, count)
    members = set(members)
    min = 9999
    result = 0
    for start in starts:
        if start[0] != 0:
            print(min)
            return
        link = members - set(start)
        result = checkAbility(start, link)
        if min > result:
            min = result


n = int(sys.stdin.readline().strip())
abilityMatrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
divTeam(n)