def kmp_search(string, text):
    found = []
    text_idx = 0
    string_idx = 0
    text_len = len(text)
    string_len = len(string)

    if string_len == 0:
        return found

    movement = calculate_movement(string)

    while (text_len - text_idx) >= (string_len - string_idx):
        if text[text_idx] == string[string_idx]:
            string_idx += 1
            text_idx += 1
        
        if string_idx == string_len:
            string_idx = movement[string_idx - 1]
            found.append(text_idx - string_len)
        elif text_idx < text_len and string[string_idx] != text[text_idx]:
            if string_idx != 0:
                string_idx = movement[string_idx - 1]
            else:
                text_idx += 1

    return found


def calculate_movement(string):
    movement = [0] * len(string)
    i = 1
    lng = 0
    movement[0] = 0
    while i < len(string):
        if string[i] == string[lng]:
            lng += 1
            movement[i] = lng
            i += 1
        else:
            if lng != 0:
                lng = movement[lng - 1]
            else:
                movement[i] = 0
                i += 1
    return movement


if __name__ == "__main__":
    a = "ACABDX"
    b = "ABABC"
    print(kmp_search(b, a))
    txt = "ABCABCABC"
    pat = "ABC"
    print(kmp_search(pat, txt))
    print(kmp_search("ABC", "ABC"))
    print(kmp_search("ABC", "ABDEF"))
    print(kmp_search("ABC", "ABD"))
    print(kmp_search("ABCD", "ABC"))
