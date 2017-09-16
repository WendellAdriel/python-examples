def test(value):
    if value < 10:
        raise ValueError("The number must be greater than 10")
    
    return value

print(test(15))
try:
    print(test(4))
except ValueError:
    print("Wrong value...")
    raise