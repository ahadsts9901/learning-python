with open("rename_me.txt") as f :
    content = f.read()

with open("rename_me_done.txt","w") as f :
    f.write(content)