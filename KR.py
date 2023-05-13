def searchKR(pattern, text):

    if not pattern or not text:
        return []
    positions = []
    m = len(pattern)
    n = len(text)
    d = 26  # Len of alphabet
    p = 0   # patern hash
    t = 0   # text hash
    h = 1   # hash comp
    q = 1013  # prime number

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        if i < len(text):
            t = (d*t + ord(text[i])) % q

    # Find the match
    for i in range(n-m+1):
        if p == t:
            # check if it is a match
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                positions.append(i)

        if i < n-m:
            # Actualize t-hash
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

    return positions
