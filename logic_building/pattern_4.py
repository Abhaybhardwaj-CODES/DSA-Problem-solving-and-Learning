class solution:
    def pattern_4(self,N):
        for i in range (N):
         print(" ")
         for j in range(N,i,-1):
           print("*" , end=" ")
        print()   

if __name__ == "__main__":
    sol = solution()

    N = 5

    sol.pattern_4(N)