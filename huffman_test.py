from huffman_tree import node, huffman_tree

#used to count the frequency of letters in a large text file

count = 0.0
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
            count += 1.0
    count_ls = []
    for key in letter_freq.keys():
        letter_freq[key] = letter_freq[key]/count
        print("KEY: %s, VAL: %f" % (key, letter_freq[key]))
        #now sort the key - val pairs as a list of tuples
        count_ls.append((key, letter_freq[key]))

#now sort the key - val pairs as a list of tuples
count_ls.sort(key=lambda tup: tup[1], reverse=True)
for i in count_ls:
    print("KEY: %s, VAL: %f" % (i[0],i[1]))

#number of characters
print("char volume: %d" % len(count_ls))

rt = node((None,None))
t = huffman_tree(rt)
t.construct_from_list_of_tuples(count_ls)
