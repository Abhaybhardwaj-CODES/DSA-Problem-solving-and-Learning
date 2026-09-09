class solution:
    def pattern_13(self,N):
        for i in range (N):
         
         for j in range(i +1):
           print(chr(65 + j) , end=" ")
         print()   

if __name__ == "__main__":
    sol = solution()

    N = 5

    sol.pattern_13(N)