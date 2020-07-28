import urllib.request
try:
    fhand = urllib.request.urlopen("https://www.python.org/")
    # print(type(fhand))
    print(fhand.read())
    count = dict()
    for line in fhand:
        words = line.decode().strip()
        for word in words:
            count[word] = count.get(word, 0)+1

    # print(count)
    fhand.close()


except Exception as e:
    print(e)
    print("WEb page not found")
    exit()
