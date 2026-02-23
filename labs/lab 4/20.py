g = 0

def outer():
    n = 0
    def inner():
        nonlocal n
        global g
        for cmd in commands:
            scope, val = cmd.split()
            val = int(val)
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            elif scope == "local":
                x = val
        return n
    n = inner()
    return n

n_commands = int(input())
commands = [input() for _ in range(n_commands)]
n = outer()
print(g, n)