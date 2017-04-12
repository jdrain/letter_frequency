class huffman_tree:

    def __init__(self,root):
        self.root = root

    def DFS(self, root):
        ls = [root]
        if self.left != None:
            dfs(self.left)
        if self.right != None:
            dfs(self.right)
        return ls

    def dfs(self, current_node, node_ls):
        ls.append(current_node)
        if current_node.left != None:
            dfs(current_node.left)
        if current_node.right != None:
            dfs(current_node.right)

    def construct_from_list_of_tuples(self,tuple_ls):
        # the second tuple val should be the one with the weighting
        # list should be sorted so in descending order
        i = len(tuple_ls) - 1
        nd = None
        nd1 = None
        top_nd = None
        while i > 0:
            # take the lowest two values and combine them into a node
            if not isinstance(tuple_ls[i],node) and not isinstance(tuple_ls[i-1],node):
                nd = node(tuple_ls[i])
                nd1 = node(tuple_ls[i-1])
            elif not isinstance(tuple_ls[i],node):
                nd = node(tuple_ls[i])
                nd1 = tuple_ls[i-1]
            elif not isinstance(tuple_ls[i-1],node):
                nd = tuple_ls[i]
                nd1 = node(tuple_ls[i-1])
            else:
                nd = tuple_ls[i]
                nd1 = tuple_ls[i-1]

            #create the combined node
            top_nd = node((None,nd.data[1]+nd1.data[1]))
            top_nd.set_right(nd)
            top_nd.set_left(nd1)

            #resize the list
            tuple_ls.remove(tuple_ls[i])
            tuple_ls.remove(tuple_ls[i-1])
            tuple_ls.append(top_nd)

            #adjust i
            i = len(tuple_ls) - 1

        self.root = top_nd

class node:

    def __init__(self,tuple_data):
        self.data = tuple_data
        self.right = None
        self.right = None

    def set_right(self,right):
        self.right = right

    def set_left(self,left):
        self.left = left

    def has_children(self):
        if self.right == None and self.right == None:
            return False
        else:
            return True
