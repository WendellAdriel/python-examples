print(set("my name is Wendell and Wendell is my name".split()))

a = set(["Jake", "John", "Peter"])
b = set(["John", "Mary"])

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))