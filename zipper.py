def BWT_zip(data):
    data += "$"
    cycles = [data[i:] + data[:i] for i in range(len(data))]
    cycles = sorted(cycles)
    output = "".join([c[-1] for c in cycles])
    return output, output.index("$")

def MTF_zip(data):
    alphabet = sorted(list(set(data)))
    output = []

    for i in range(len(data)):
        output.append(alphabet.index(data[i]))
        alphabet.remove(data[i])
        alphabet.insert(0, data[i])
    
    return output

def RLE_zip(data):
    pass

def zip_file(file_content: bytes) -> bytes:
    data = file_content.decode('utf-8')
    bwt_data, index = BWT_zip(data)
    print(bwt_data, index)
    mtf_data = MTF_zip(bwt_data)
    print(mtf_data)
    rle_data = RLE_zip(mtf_data)
    print(rle_data)

def unzip_file(zipped_file_content: bytes) -> bytes:
    pass


def main():
    string = b"banana"
    zip_file(string)

if __name__ == "__main__":
    main()