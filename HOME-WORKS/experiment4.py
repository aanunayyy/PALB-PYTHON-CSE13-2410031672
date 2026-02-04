def union_arrays(a, b):
    seen = {}

    for x in a:
        seen[x] = 1

    for x in b:
        seen[x] = 1

    return list(seen.keys())
