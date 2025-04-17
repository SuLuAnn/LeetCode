def kmp_search(text: str, pattern: str) -> bool:
    # Step 1: 產生 prefix table
    lps = build_lps(pattern)

    # Step 2: 開始匹配過程
    i = 0  # 指向 text
    j = 0  # 指向 pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            # 匹配成功
            if j == len(pattern):
                return True
        else:
            if j != 0:
                j = lps[j - 1]  # 往回跳
            else:
                i += 1  # 沒得跳，只能前進 text

    return False

def build_lps(pattern: str) -> list[int]:
    lps = [0] * len(pattern)
    length = 0  # 當前最長的 prefix-suffix 長度

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # 繼續往前找
            else:
                lps[i] = 0
                i += 1

    return lps

if __name__ == "__main__":
    text = "abxabcabcaby"
    pattern = "abcaby"

    print(kmp_search(text, pattern))  # True

