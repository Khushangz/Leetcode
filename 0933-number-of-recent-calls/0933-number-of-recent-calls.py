class RecentCounter:

    def __init__(self):
        self.time=[]
        self.count=0

    def ping(self, t: int) -> int:
        A=self.time
        B=[]
        A.append(t)
        k=0
        for i in range(len(A)):
            if t-A[i]<= 3000:
                k=i
                break
        self.time=A[k:]
        self.count=len(A[k:])
        return self.count



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
