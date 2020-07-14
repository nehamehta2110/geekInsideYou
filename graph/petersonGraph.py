"""
Peterson is a special type of graph and we have to find out whether a given walk is
possible or not
eg. ABB
output 016
"""
result = [0]

adj = [[False for i in range(10)] for j in range(10)]


def findWalk(walk, v):
    result[0] = v

    for i in range(1, len(walk)):
        if (adj[v][ord(walk[i]) - ord('A')] or
                adj[ord(walk[i]) - ord('A')][v]):
            v = ord(walk[i]) - ord('A')

        elif (adj[v][ord(walk[i]) - ord('A') + 5] or
              adj[ord(walk[i]) - ord('A') + 5][v]):
            v = ord(walk[i]) - ord('A') + 5

        else:
            return False
        result.append(v)
    return True


def define():
    adj[0][1] = adj[1][2] = adj[2][3] = \
        adj[3][4] = adj[4][0] = adj[0][5] = \
        adj[1][6] = adj[2][7] = adj[3][8] = \
        adj[4][9] = adj[5][7] = adj[7][9] = \
        adj[9][6] = adj[6][8] = adj[8][5] = True

    walk = 'ABB'

    walk = list(walk)

    if findWalk(walk, ord(walk[0]) - ord('A')) or findWalk(walk, ord(walk[0]) - ord('A') + 5):
        print(*result, sep="")
    else:
        print('-1')


if __name__ == '__main__':
    define()
