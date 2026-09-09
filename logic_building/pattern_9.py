class solution:
    def erected_Triangle(self,N):
        for i in range(N):
            print("*" * (i + 1) )
    def inserted_Triangle(self , N):
        for i in range(N ,0 , -1):       
            print("*" * i)  

if __name__ == "__main__":
    obj = solution()
    N = 6
    obj.erected_Triangle(N)        
    obj.inserted_Triangle(N)
     