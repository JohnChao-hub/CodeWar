## Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    temp = {}
    res = []
    for i in order:
      if i not in temp :
        temp[i] = 0
      else:
        temp[i] += 1
      if temp[i] < max_e:
        res.append(i)
    return res

delete_nth([1,2,3,1,2,3,1,2,5], 2)

#sol2
def delete_nth2(order,max_e):
    if not order or max_e < 1:
        return []

    counted_order = { x:0 for x in order }
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order

{ x:0 for x in [1,2,3,1,2,3,1,2,5] } #In dict, key is unique