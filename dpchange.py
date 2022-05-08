def mincoins(n,a,dp):  #n=money a = denominations
    ans=float("inf")
    
    if n==0:
        return 0
    else:
        for i in range(len(a)):                 
            if n-a[i] >=0:              # 18-7=11
                if dp[n-a[i]] !=-1:     # dp[11] = 1
                    subans=dp[n-a[i]]   #   subans=1
                else:

                    subans = mincoins(n-a[i],a,dp)
                if (subans +1) < ans:
                    ans=subans+1        #
        dp[n]=ans
        print(dp[n]-1)
        return ans

n=18
a=[7,5,1]

dp=[-1]*(n+1)
dp[0]=0
print(mincoins(n,a,dp))

