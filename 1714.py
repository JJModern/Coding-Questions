class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        MOD = 10 ** 9+7
        sqrtN = int(N**0.5)

        dp = [[0] * N for _ in range(sqrtN)]
        for i in range(1, sqrtN):
            for j in range(N - 1, -1, -1):
                if(dp[i][j] == 0):
                        dp[i][j] = nums[j]
                if i + j < N:
                    dp[i][j] += dp[i][i+j]
                    dp[i][j] %= MOD
        res = []
        for x, y in queries:
            if(y < sqrtN):
                res.append(dp[y][x])
            else:
                # print(nums[x::y])
                res.append(sum(nums[x::y])% MOD)
        return res

        # MOD = 10 ** 9 + 7
        # N = len(nums)
        # big = 0
        # for f, s in queries:
        #     big = max(big, s)
        # dp = [[0] * N for _ in range(big+1)]
        # # max of second queries
        # for y in range(1, big+1):
        #     for x in range(N-1, -1, -1):
                # if(dp[i][j] == 0):
                #         dp[i][j] = nums[j]
                # if i+j < N:
                #     dp[i][j] += dp[i][i+j]
                #     dp[i][j] %= MOD

        # # print(dp)
        # res = []
        # for x, y in queries:
        #     res.append(dp[y][x])
        # return res

        #         if(x == N-1):
        #             if(x % y == 0):
        #                 dp[y][x] = nums[x] % MOD
        #         else:
        #             if(x % y == 0):
        #                 if(y + x < N):
        #                     dp[y][x] = (nums[x] + dp[y][x+y]) % MOD
        #                 else:
        #                     dp[y][x] = (nums[x]) % MOD
        #             else:
        #                 dp[y][x] = (dp[y][x+1] % MOD)