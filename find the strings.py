def countPerms(n):
    
 MOD=1e9 +7
 dp=[[0 for i in range(5)]for j in range(n+1)]
 for i in range(5):
        dp[1][i]=1
 relation=[[1],[0,2],[0,1,3,4],[2,4],[0]]
 for i in range(1,n,1):
        for u in range(5):
            dp[i+1][u]=0
            for v in relation[u]:
                dp[i+1][u]+=dp[i][v]%MOD
 ans=0
 for i in range(5):
        ans=(ans+dp[n][i])%MOD
 return int(ans)