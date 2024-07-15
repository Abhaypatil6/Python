l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l)
# l.append(7)                   # add 7 in list
# l.sort(reverse=True)          # arrange then reverse
# l.reverse()                   # reverse
# print(l.index(1))             # 1 is on index 2
# print(l.count(1))             # no. of 1 in list
m = l.copy()                  # copying the list so that actual list value should not change 
# m[0] = 0
# l.insert(1, 899)                # at index 1 insert value 899
m = [900, 1000, 1100]
k = l + m
# print(k)
l.extend(m)
print(l)
print(m)