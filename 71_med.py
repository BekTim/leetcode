path = "/.../a/../b/c/../d/./"
stack = []

for token in path.split('/'):
    if token == "" or token == ".":
        continue
    elif token == "..":
        if stack:
            stack.pop()
    else:
        stack.append()
return "/" + "/".join(stack)


    





'''

for r in range(len(path)):
    res.append(path[r])

    if path[r] == "/" and r+1 != len(path) and path[r+1] == "/":
        res.pop()

    if path[r] == "." and r+1 != len(path) and path[r+1] == "." and path[r+2] != '.' and path[r-1] != ".":
        res.pop() # for .
        res.pop() # for /
        j = len(res) - 1 
        while res[j] != "/":
            res.pop()
            j = j - 1

    if path[r] == "." and r+1 != len(path) and path[r+1] == "/":
        res.pop()
        res.pop()

    print(res)

edge_slash = len(res) - 1
if res[edge_slash] == "/":
    res.pop()

print(len(res))
print(res)
'''