def longesCommonPrefix(words):
    repeated_letters = ""

    for w in range(len(words[0])):
        for s in words:
            if w == len(s) or s[w] != words[0][w]:
                return repeated_letters
        repeated_letters += words[0][w]
    return repeated_letters






strs = ["flower","flow","flight"]
print(longesCommonPrefix(strs))







