def isSolvable(words, result):

    mp = [-1]*(26)
    used = [0]*(10)
    Hash = [0]*(26)
    CharAtfront = [0]*(26)
    uniq = ""
    for word in range(len(words)):
        for i in range(len(words[word])):
            ch = words[word][i]
            Hash[ord(ch) - ord('A')] += pow(10, len(words[word]) - i - 1)
            if mp[ord(ch) - ord('A')] == -1:
                mp[ord(ch) - ord('A')] = 0
                uniq += str(ch)
            if i == 0 and len(words[word]) > 1:
                CharAtfront[ord(ch) - ord('A')] = 1
    for i in range(len(result)):
        ch = result[i]
        Hash[ord(ch) - ord('A')] -= pow(10, len(result) - i - 1)
        if mp[ord(ch) - ord('A')] == -1:
            mp[ord(ch) - ord('A')] = 0
            uniq += str(ch)
        if i == 0 and len(result) > 1:
            CharAtfront[ord(ch) - ord('A')] = 1

    mp = [-1]*(26)

    return solve(uniq,0,0,mp,used,Hash,CharAtfront)
def solve(words, i, S, mp, used, Hash, CharAtfront):
    # If i is word.length
    if i == len(words):
        return S == 0, mp

    ch = words[i]
    val = mp[ord(words[i]) - ord('A')]

    if val != -1:
        return solve(words, i + 1, S + val * Hash[ord(ch) - ord('A')], mp, used, Hash, CharAtfront)
    x = False
    for l in range(10):
        if CharAtfront[ord(ch) - ord('A')] == 1 and l == 0:
            continue
        if used[l] == 1:
            continue
        mp[ord(ch) - ord('A')] = l
        used[l] = 1

        y = solve(words, i + 1, S + l * Hash[ord(ch) - ord('A')], mp, used, Hash, CharAtfront)
        x =y[0]| x
        if x:
            return y
        mp[ord(ch) - ord('A')] = -1
        used[l] = 0
    return x,mp
arr = [ "MIT", "MANIPAL" ]
S = "MITMAHE"
t,r = isSolvable(arr,S)
if t:
    for i in range(26):
        if r[i] != -1:
             print(f'{chr(i+65)}:{r[i]}')
else:
	print("No Can't Do!")