from KR import searchKR
# from N import ...... as searchN
# from KMP import ...... as searchKMP
from random import randint, choice


def create_test_case():
    size = randint(1, 100)
    text = ''
    pattern = ''

    for i in range(size):
        text += choice(['A', 'B'])

    size = randint(1, size//10)
    for i in range(size):
        pattern += choice(['A', 'B'])

    return text, pattern


def test_empty_text():
    text = ""
    pattern = "CDD"
    pattern_pos_list_KR = searchKR(pattern, text)
    assert pattern_pos_list_KR == []
    # pattern_pos_list_KMP = searchN(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == []
    # assert pattern_pos_list_KMP == []


def test_empty_pattern():
    text = "ABCCDDAEFG"
    pattern = ""
    pattern_pos_list_KR = searchKR(pattern, text)
    assert pattern_pos_list_KR == []
    # pattern_pos_list_KMP = searchN(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == []
    # assert pattern_pos_list_KMP == []


def test_empty_both():
    text = "ABCCDDAEFG"
    pattern = ""
    pattern_pos_list_KR = searchKR(pattern, text)
    assert pattern_pos_list_KR == []
    # pattern_pos_list_KMP = searchN(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == []
    # assert pattern_pos_list_KMP == []


def test_pattern_equals_text():
    text = "ABCCDDAEFG"
    pattern = "ABCCDDAEFG"
    pattern_pos_list_KR = searchKR(pattern, text)
    assert pattern_pos_list_KR == [0]
    # pattern_pos_list_KMP = searchN(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == [0]
    # assert pattern_pos_list_KMP == [0]


def test_pattern_longer_then_text():
    text = "ABCCDDAEFG"
    pattern = "ABCCDDAEFGH"
    pattern_pos_list_KR = searchKR(pattern, text)
    assert pattern_pos_list_KR == []
    # pattern_pos_list_KMP = searchN(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == []
    # assert pattern_pos_list_KMP == []


def test_pattern_does_not_occur_in_text():
    text = "ABCCDDAEFG"
    pattern = "ZX"
    pattern_pos_list_KR = searchKR(pattern, text)
    assert pattern_pos_list_KR == []
    # pattern_pos_list_KMP = searchN(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == []
    # assert pattern_pos_list_KMP == []


def test_typical_1():
    text = "ABCDEFFFABC"
    pattern = "ABC"
    # pattern_pos_list_N = searchN(pattern, text)
    pattern_pos_list_KR = searchKR(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == pattern_pos_list_KR
    # assert pattern_pos_list_N == pattern_pos_list_KMP
    assert pattern_pos_list_KR == [0, 8]


def test_typical_2():
    text = "AAAAAAA"
    pattern = "AA"
    # pattern_pos_list_N = searchN(pattern, text)
    pattern_pos_list_KR = searchKR(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == pattern_pos_list_KR
    # assert pattern_pos_list_N == pattern_pos_list_KMP
    assert pattern_pos_list_KR == [0, 1, 2, 3, 4, 5]


def test_typical_3():
    text = "ABCdABCABCdABCABCd"
    pattern = "ABCd"
    # pattern_pos_list_N = searchN(pattern, text)
    pattern_pos_list_KR = searchKR(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == pattern_pos_list_KR
    # assert pattern_pos_list_N == pattern_pos_list_KMP
    assert pattern_pos_list_KR == [0, 7, 14]


def test_random():
    text, pattern = create_test_case()
    # pattern_pos_list_N = searchN(pattern, text)
    pattern_pos_list_KR = searchKR(pattern, text)
    # pattern_pos_list_KPM = searchKMP(pattern, text)
    # assert pattern_pos_list_N == pattern_pos_list_KR
    # assert pattern_pos_list_N == pattern_pos_list_KMP
