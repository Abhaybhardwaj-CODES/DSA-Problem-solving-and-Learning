class solution:
    def erected_triangle(self,N):
        for i in range(N):
            print(" " * (N - i - 1), end="")
            # Print stars
            print("*" * (2 * i + 1), end="")
            # Print spaces after stars
            print(" " * (N - i - 1))
         
    def inverted_triangle(self,N):
         for i in range(N):
            # Print spaces before stars
            print(" " * i, end="")
            # Print stars
            print("*" * (2 * N - (2 * i + 1)), end="")
            # Print spaces after stars
            print(" " * i)
         print()


if __name__ == "__main__":
   N = 6  
   obj = solution()
   obj.erected_triangle(N)
   obj.inverted_triangle(N)