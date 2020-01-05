start = '246666'
end = '779999'
int_start = int(start)
int_end = int(end)
i = int_start

def print_the_numbers():
    count = 0
    for a in range(2, 10):
        if a > 2:
            for b in range(a, 10):
                for c in range(b, 10):
                    for d in range(c, 10):
                        for e in range(d, 10):
                            for f in range(e, 10):
                                if (a<b and b<c and c<d and d<e and e<f):
                                    continue
                                count += 1
                                num = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                                i = int(num)
                                print(num)
                                if i >= int_end:
                                    return count 
        else:
            for b in range(4, 10):
                if b > 4:
                    for c in range(b, 10):
                        for d in range(c, 10):
                            for e in range(d, 10):
                                for f in range(e, 10):
                                    if (a<b and b<c and c<d and d<e and e<f):
                                        continue
                                    count += 1
                                    num = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                                    i = int(num)
                                    print(num)
                                    if i >= int_end:
                                        return count 
                else:
                    for c in range(6, 10):
                        for d in range(c, 10):
                            for e in range(d, 10):
                                for f in range(e, 10):
                                    if (a<b and b<c and c<d and d<e and e<f):
                                        continue
                                    count += 1
                                    num = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                                    i = int(num)
                                    print(num)
                                    if i >= int_end:
                                        return count 
            

print(print_the_numbers())