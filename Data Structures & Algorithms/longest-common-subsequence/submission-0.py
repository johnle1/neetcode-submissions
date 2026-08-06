class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp =[[None for _ in range(n+1)]for _ in range(m+1)]
        
        def dfs(i, j, s1, s2, dp):
            if i == len(s1) or j == len(s2):
                return 0
    
            if dp[i][j] is not None:
                return dp[i][j]
    
            if s1[i] == s2[j]:
                # Add 1 for the matching character and return immediately
                dp[i][j] = 1 + dfs(i+1, j+1, s1, s2, dp)
                return dp[i][j]
                
            down = dfs(i+1, j, s1, s2, dp)
            left = dfs(i, j+1, s1, s2, dp)
            
            # Assign first, then return (with the typo fixed)
            dp[i][j] = max(down, left)
            return dp[i][j]
        return dfs(0,0,text1,text2,dp)


        
        