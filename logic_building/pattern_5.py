class solution:
    def pattern_5(self,N):
        for i in range (N):
         print(" ")
         for j in range(N,i,-1):
            print(N - j + 1, end=" ")
        print()   

if __name__ == "__main__":
    sol = solution()

    N = 5

    sol.pattern_5(N)