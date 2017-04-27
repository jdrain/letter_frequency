import json
import huffman_tree
import sys

def get_frequency_ls(src_file):
    letter_freq = {}
    with open(src_file,"r") as f:
        for line in f:
            for key in line:
                if key in letter_freq:
                    letter_freq[key] += 1
                else:
                    letter_freq[key] = 1
    
    #create and sort list
    count_ls = [(key,letter_freq[key]) for key in letter_freq.keys()]
    count_ls.sort(key=lambda tup: tup[1], reverse=True)
    return count_ls

#write the ls into a json for storage
def get_json_from_txt_file(src_file,out_json):
    freq_ls = get_frequency_ls(src_file)
    dic = {src_file:freq_ls}
    s = json.dumps(dic,indent=4)
    with open(out_json,'w+') as f:
        f.write(s)

def get_ls_from_file(src_file):
    with open(src_file,'r') as f:
        data = json.load(f)
        ls = [data[i] for i in data.keys()]
    return ls

def create_tree_from_frequency_ls(src_file):
    ls = get_ls_from_file(src_file)
    if (len(ls) > 1):
        print("Expected a list with only one element")
        return None
    else:
        #make the list one dimensional
        ls = ls[0]
        
        #initialize the tree
        rt = node((None,None))
        t = huffman_tree(rt)
        t.create_tree_from_frequency_ls(ls)
        return t
