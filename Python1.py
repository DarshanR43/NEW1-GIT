def sum():
    n=input("")
    for i in n:
        if i in ["A","a","E","e","I","i","O","o","U","u"]:
            n=n.replace("*")
sum()