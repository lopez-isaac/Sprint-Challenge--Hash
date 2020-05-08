def finder(files, queries):

    cache = {}
    result = []

    for i in files:
        cache[i] = i

    for key in cache:
        filename = cache[key][-3:]
        if filename in queries:
            result.append(key)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
