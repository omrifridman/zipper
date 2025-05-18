def BWT_zip(data):
    data += "$"
    cycles = [data[i:] + data[:i] for i in range(len(data))]
    cycles = sorted(cycles)
    output = "".join([c[-1] for c in cycles])
    return output, output.index("$")

def zip_file(file_content: bytes) -> bytes:
    data = file_content.decode('utf-8')
    bwt_data = BWT_zip(data)
    print(bwt_data)

def unzip_file(zipped_file_content: bytes) -> bytes:
    pass


def main():
    string = b"banana"
    zip_file(string)

if __name__ == "__main__":
    main()