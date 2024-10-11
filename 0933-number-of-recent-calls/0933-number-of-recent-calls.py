class RecentCounter:

    def __init__(self):
        self.time=[]

    def ping(self, t: int) -> int:
        A=self.time
        A.append(t)
        k=0
        for i in range(len(A)):
            if t-A[i]<= 3000:
                k=i
                break
        self.time=A[k:]
        return len(A[k:])



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
