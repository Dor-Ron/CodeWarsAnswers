def unused_digits(*args):
    used = "".join([str(arg) for arg in args])
    return "".join([str(num) for num in filter(lambda x: str(x) not in used, range(10))])

# could be one-lined as follows: return "".join([str(num) for num in filter(lambda x: str(x) not in "".join([str(arg) for arg in args]), range(10))])
