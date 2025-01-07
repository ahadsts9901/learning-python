with open("poem.txt") as f:
    content = f.read()
    if("mern" in content):
        print("word mern is available in content")
    else:
        print("word mern is not available in content")
