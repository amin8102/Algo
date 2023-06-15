import heapq


class Node:
    
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, other):
        # compares the value of each char 
        return self.freq < other.freq


def printNodes(node, val=''):
    #print the char and huff code for that char
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


def encodeHuffman(root, input_str):
    #translate the string with our tree and returns huff code of our string
    encoding_dict = {}
    generateEncodingDict(root, '', encoding_dict)
    encoded_str = ''
    for char in input_str:
        encoded_str += encoding_dict[char]
    return encoded_str


def generateEncodingDict(node, code, encoding_dict):
    #creat the code for each char 
    if node is None:
        return
    if node.left is None and node.right is None:
        encoding_dict[node.symbol] = code
    generateEncodingDict(node.left, code + '0', encoding_dict)
    generateEncodingDict(node.right, code + '1', encoding_dict)


def decodeHuffman(root, encoded_str):
    #using our tree this func will return the string for our code
    decoded_str = ""
    curr = root
    for bit in encoded_str:
        if bit == '0':
            curr = curr.left
        elif bit == '1':
            curr = curr.right

        if curr.left is None and curr.right is None:
            decoded_str += curr.symbol
            curr = root

    return decoded_str


input_str = input("Enter the string to encode: ")

freq = {}
for char in input_str:
    freq[char] = freq.get(char, 0) + 1
#creating our tree:)
nodes = []
for char, frequency in freq.items():
    heapq.heappush(nodes, Node(frequency, char))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = '0'
    right.huff = '1'
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newNode)

huffman_tree_root = nodes[0]
print("\nHuffman Tree:")
printNodes(huffman_tree_root)

encoded_string = encodeHuffman(huffman_tree_root, input_str)
print("\nEncoded String:", encoded_string)

decoded_string = decodeHuffman(huffman_tree_root, encoded_string)
print("\nDecoded String:", decoded_string)
