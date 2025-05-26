import heapq
import math
from collections import Counter
from bitarray import bitarray
import json

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

    shaved_blocks = [block[:n].to01() for block in blocked_data]
    counts = Counter(shaved_blocks)
    heap = [Node(block, count) for block, count in counts.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, left.key + right.key, left, right))
    
    dictionary = build_dict(heapq.heappop(heap))
    huffmanized = bitarray()
    for i in [dictionary[block[:n].to01()] + block[n:] for block in blocked_data]:
        huffmanized += i

    return huffmanized, dictionary, p

def my_unzip(binary_data, milon, p, r):
    i = 0
    true_data = bitarray()
    size = len(binary_data)
    current = bitarray()
    
    reverse_dict = {v.to01(): k for k, v in milon.items()}
    
    while i < size:
        current.append(binary_data[i])
        temp = current.copy().to01()
        if temp in reverse_dict:
            byte = reverse_dict[temp]
            true_data += bitarray(byte)
            i += 1
            if r > 0:
                true_data += binary_data[i:i + r]
                i += r
            current = bitarray()
        else:
            i += 1
    
    return true_data[:-p] if p > 0 else true_data

def make_file(data, dictionary, p, r):
    print(dictionary)
    dictionary = {v: k.to01() for v, k in dictionary.items()}

    output = bitarray()
    output.frombytes(f"{p},{r},{json.dumps(dictionary)}".encode("utf-8"))
    output.frombytes(b"\x00")
    output += data

    return output.tobytes()

def get_from_file(bytes_data):
    print(bytes_data)
    start, data = bytes_data.split(b"\00")
    print(start)
    print(data)
    print("fuck")
    d = start.decode()
    p, r, dictionary = int(d.split(",")[0]), int(d.split(",")[1]), ",".join(d.split(",")[2:])
    print(p)
    print(r)
    print(dictionary)
    print("sdfsdf")
    dictionary = json.loads(dictionary)
    dictionary = {v: bitarray(k) for v, k in dictionary.items()}
    print(dictionary)
    bits = bitarray()
    bits.frombytes(data)

    return bits, dictionary, p, r

def compress(data):
    n, r = 8, 0
    data, dictionary, p = my_zip(data, n, r)
    return make_file(data, dictionary, p, r)

def decompress(data):
    data, dictionary, p, r = get_from_file(data)
    return my_unzip(data, dictionary, p, r).tobytes()

def main():
    print(decompress(compress(b"hello world!")))

if __name__ == "__main__":
    main()