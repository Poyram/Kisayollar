def sayı(x1):
    li = [x1]
    kü = set()
    while True:
        if len(li) > 1:
            kü.add(str(sorted(li, reverse=True)))
        if len(li) == x1:
            break
        for i in range(len(li)):
            i += 1
            if li[len(li)-i] != 1:
                li[len(li)-i] -= 1
                if len(li) == 1 or len(li) <= len(li)-i+1:
                    li.append(1)
                else:
                    li[len(li)-i+1] += 1
                break
    print(len(kü))
        
sayı(100)
