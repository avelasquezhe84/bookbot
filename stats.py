def get_num_words(book_content):
    word_count = len(book_content.split())
    return word_count


def get_char_count(book_content):
    char_count = {}
    for c in book_content:
        char_count[c.lower()] = char_count.get(c.lower(), 0) + 1
    return char_count


def sort_on(_dict):
    return _dict["num"]


def get_char_count_report(char_dict):
    report_list = []
    for k, v in char_dict.items():
        c_dict = {"char": k, "num": v}
        report_list.append(c_dict)
    report_list.sort(reverse=True, key=sort_on)
    return report_list