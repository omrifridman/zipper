import heapq
import math
from collections import Counter
from bitarray import bitarray

class Node:
    def __init__(self, data, key, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.key < other.key

def build_dict(node, d={}, current=bitarray()):
    if node.data is not None:
        d[node.data] = current
        return d
    
    d = build_dict(node.left, d, current + bitarray('0'))
    d = build_dict(node.right, d, current + bitarray('1'))

    return d

# n - huffman
# r - remainder
# p - padding
def my_zip(bytes_array, n, r):
    data = bitarray()
    data.frombytes(bytes_array)

    p = (math.ceil(len(data) / (n+r)) * (n+r)) - len(data)
    data += [0] * p
    blocked_data = [data[i*(n+r):(i+1)*(n+r)] for i in range(len(data) // (n+r))]
    print(blocked_data)

    shaved_blocks = [block[:n].tobytes() for block in blocked_data]
    counts = Counter(shaved_blocks)
    heap = [Node(block, count) for block, count in counts.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, left.key + right.key, left, right))
    
    dictionary = build_dict(heapq.heappop(heap))
    huffmanized = bitarray()
    for i in [dictionary[block[:n].tobytes()] + block[n:] for block in blocked_data]:
        huffmanized += i

    return huffmanized, dictionary


print(my_zip(b"hello world!", 8, 0))
bits = bitarray()
bits.frombytes(b"hello world!")
print(bits)