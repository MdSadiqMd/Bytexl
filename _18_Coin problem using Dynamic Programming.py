def count(coins,n,sum):
    if (sum==0):
        return 1
    if(sum<0):
        return 0
    if(n<=0):
        return 0
    return count(coins,n,sum)+count(coins,n,sum-coins[n-1])
coins=[1,2,3]
n=len(coins)
print(count(coins,n,4))
print("commit sake")
print("")