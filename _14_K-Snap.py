<<<<<<< HEAD
class solution:
    def solve(self,weigths,values,capacity):
        res=0
        for pair in sorted(zip(weights,values),key=lambda x:-x[1]/x[0]):
            if not bool(capacity):
                break
            if pair[0]>capacity:
                res+=int(pair[1]/(pair[0]/capacity))
                capacity=0
            elif pair[0]<=capacity:
                res+=pair[1]
                capacity-=pair[0]
        return int(res)
ob=solution()
weights=[6,7,3]
values=[110,120,2]
capacity=10
print(ob.solve(weights,values,capacity))
=======
class solution:
    def solve(self,weigths,values,capacity):
        res=0
        for pair in sorted(zip(weights,values),key=lambda x:-x[1]/x[0]):
            if not bool(capacity):
                break
            if pair[0]>capacity:
                res+=int(pair[1]/(pair[0]/capacity))
                capacity=0
            elif pair[0]<=capacity:
                res+=pair[1]
                capacity-=pair[0]
        return int(res)
ob=solution()
weights=[6,7,3]
values=[110,120,2]
capacity=10
print(ob.solve(weights,values,capacity))
>>>>>>> 6d4c0bdaf237af1555cf484289d2fa8b6668d854
