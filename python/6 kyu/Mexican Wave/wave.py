def wave(people):
    answer = []
    
    n = 0
    if people.lstrip() == "":
        return answer
    else:
        while n < len(people):
            if people[n] != " ":
                answer.append(''.join([people[:n], people[n].upper(), people[n + 1:]]))
                print(''.join([people[:n], people[n].upper(), people[n + 1:]]))
            
            n = n+1
        return answer