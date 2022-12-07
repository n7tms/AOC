# understanding the use of next and enumerate in this context

data = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

# print(next(i for i,c in enumerate(data) if len(set(data[i-4:i]))==4))

# It appears that this is essentially a for loop that "loops" through the data until if finds
# four unique letters. "next" keeps the loop going. enumerate returns an index (i) and a 
# value (c). i is used to index the data and is eventually returned as the answer.


list1 = [1,2,3,4,5]
l_list = enumerate(list1)
print(next(l_list))

list2 = ['a','b','c','d']
for count, value in enumerate(list2,start=1):
    print(count, value)

def even_items(iterable):
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values

# The following three lines of code all out put ['b', 'd']
print(even_items(list2))
print([v for i,v in enumerate(list2,start=1) if not i % 2])
print(list2[1::2])

a = list2[1::2]
print(a)


