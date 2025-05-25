import heapq



def myunzip(binary_data, milon, p, r):
    i = 0
    true_data = []
    size = len(binary_data)
    while i < size:
        bword = ""
        bword += binary_data[i]
        real = next((k for k, v in milon.items() if v == bword), None)
        if (real is not None):
            true_data.append(real+binary_data[i+1:i+r+1])
            i+=(r+1)
        i+=1
    return ''.join(true_data[:size-p-1])



