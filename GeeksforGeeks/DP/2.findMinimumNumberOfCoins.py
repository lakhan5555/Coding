''' Given a value V, if we want to make change for V cents, and we have infinite supply
of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to
make the change?
'''

''' Bottom up Approach '''

def minCoins(coins,m,V):
    table = [float("inf")]*(V+1)
    table[0] = 0

    for i in range(1,V+1):
        for j in range(m):
            if coins[j] <= i:
                sys_res = table[i-coins[j]]
                if sys_res != float("inf") and sys_res+1 < table[i]:
                    table[i] = sys_res + 1

    return table[V]

if __name__ == "__main__":
    coins = [9,6,5,1]
    m = len(coins)
    V = 11
    print("Minimum coins required: ",minCoins(coins,m,V))
