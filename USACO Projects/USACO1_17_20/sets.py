a = [1,4]
print(a)
print(type(a))
a = set(a)
print(a)
print(type(a))
b = {2,3,4}
share = not a.isdisjoint(b)
print(share)
d = {1,3}
if(share):
    c = a.union(b)
    print(c)
    print(d.issubset(c))
print(2 in d)
d.update({2})
print(d)
print(2 in d)
