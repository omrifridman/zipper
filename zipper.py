def zip_file(file_content: bytes) -> bytes:
    pass

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



    