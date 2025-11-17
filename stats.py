def get_num_words(text_string):
    words = len(text_string.split())
    return words


def get_ch_dict(text_string):
    chars = {}
    for ch in text_string:
        ch_lowered = ch.lower()
        if ch_lowered in chars:
            chars[ch_lowered] += 1
        else:
            chars[ch_lowered] = 1
    return chars


def char_dict_to_sorted_list(chars):
    char_list = []
    for k, v in chars.items():
        char_list.append({"char": k, "num": v})

    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list


