def naive_search(string, text):
    if not string or not text:
        return []
    asw = []
    M = len(string)
    N = len(text)

    for i in range(N - M + 1):
        j = 0

        while (j < M):
            if (text[i + j] != string[j]):
                break
            j += 1

        if (j == M):
            asw.append(i)
    return asw


# def main():
#     with open('pan_tadeusz.txt', 'r') as file:
#         text = file.read()
#     string = "które"
#     asnwers = naive_search(string, text)
#     print(asnwers)


# if __name__ == '__main__':
#     main()
