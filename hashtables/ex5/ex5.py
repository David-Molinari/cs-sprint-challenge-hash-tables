# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    ends = {}
    result = []
    for i in files:
        end_start = i.rfind("/") + 1
        end = i[end_start:]
        checker = ends.get(end)
        if checker == None:
            ends[end] = i
        else:
            new = []
            if ends[end] == list:
                for a in ends[end]:
                    new.append(a)
                new.append(i)
                ends[end] = new
            elif ends[end] != None:
                new.append(ends[end])
                new.append(i)
                ends[end] = new
            else:
                ends[end] = i
    for e in queries:
        found = ends.get(e)
        if type(found) == list:
            for li in found:
                result.append(li)
        elif found != None:
            result.append(found)
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
