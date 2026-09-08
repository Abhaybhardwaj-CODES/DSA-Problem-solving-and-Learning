class solution:
    def pattern_2(self,N):
        for i in range (1,N+1):
         print(" ")
         for j in range(1,i+1):
           print(j , end=" ")
        print()   

if __name__ == "__main__":
    sol = solution()

    N = 5

    sol.pattern_2(N)