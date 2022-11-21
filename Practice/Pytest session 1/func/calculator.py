def add(a,b):
    return a + b











def add_integers(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise ValueError("a and b should be integers")