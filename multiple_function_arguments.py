def test(first, second, third, *others):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("Others: %s" % list(others))

test(1, 2, 3, 4, 5)

def foo(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))
    
    if options.get("number") == "first":
        return first

result = foo(1, 2, 3, action = "sum", number = "first")
print("The result is: %d" % result)