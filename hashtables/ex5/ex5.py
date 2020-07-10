def finder(files, queries):
    # cache for our paths
    paths = {}
    result = []

    # iterate over our files and add to our cache
    for path in files:
        # split up path and grab just the filename
        name = path.split('/')[-1]
        
        # if our filename is not yet in our cache, add it
        if name not in paths:
            paths[name] = []

        # append full path as value to key of filename
        paths[name].append(path)

    # iterate over our list of queries and extend our result list if
    # our query is in our paths cache
    for query in queries:
        if query in paths:
            result.extend(paths[query])
    
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
