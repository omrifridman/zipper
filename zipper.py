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

def unbtw_file(btw_str, index):
    rank_S = []
    seen = {}

    for c in btw_str:
        seen[c] = seen.get(c, 0) + 1
        rank_S.append(seen[c])
    first_accur = {}
    for i, c in enumerate(sorted(btw_str)):
        if c not in first_accur:
            first_accur[c] = i
    res = []
    i = index
    for _ in range(len(btw_str)):
        res.append(btw_str[i])
        i = first_accur[btw_str[i]]+rank_S[i]-1
    return ''.join(reversed(res))

def main():
    string = b"banana"
    zip_file(string)

if __name__ == "__main__":
    main()




    