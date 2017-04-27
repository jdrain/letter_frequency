from huffman_tree import node, huffman_tree

#count the frequency of letters in a large text file
count = 0
letter_freq = {}
with open("big.txt","r") as f:
    for line in f:
        for key in line:
            if key in letter_freq.keys():
                #update the counter
                letter_freq[key] += 1
            else:
                #initialize the key
                letter_freq[key] = 1
            count += 1
    count_ls = [(key,letter_freq[key]) for key in letter_freq.keys()]

#now sort the key - val pairs as a list of tuples
count_ls.sort(key=lambda tup: tup[1], reverse=True)
print("\nSorted list of <key, val> pairs")
for i in count_ls:
    print("KEY: %s, VAL: %d" % (i[0],i[1]))

#number of characters
print("\nchar volume: %d" % len(count_ls))

# test tree construction and breadth first traversal
# bft should yield the frequency in descending order
rt = node((None,None))
t = huffman_tree(rt)
t.construct_from_list_of_tuples(count_ls)
traversal = t.BFT()
print("\nBreadth First Traversal: \n")
for i in traversal:
    print("KEY: %s VAL: %d" % (i.data[0],i.data[1]))
