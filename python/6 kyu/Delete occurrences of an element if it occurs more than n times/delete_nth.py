def delete_nth(order,max_e):
    #var
    array = []
    
    for i in order:
        if array.count(i) != max_e:
            array.append(i)
            
    return array