class solutions:
 def pattern_7(self,N):
     for i in range(N):

            # Print leading spaces
            for j in range(i):
                print(" ", end="")

            # Print stars
            for j in range(2 * N - (2 * i + 1)):
                print("*", end="")

            # Print trailing spaces
            for j in range(i):
                print(" ", end="")

            # Move to next row
            print()

if __name__ == "__main__":
    sol = solutions()
    N = 6
    sol.pattern_7(N)

           