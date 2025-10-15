def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_lower = text.lower()
    counts = {}
    for n in text_lower:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1
    return counts

def sorter(items):
    return items["num"]

def sorted_list(text):
    sorted_list = []
    for ch in text:
        sorted_list.append({"char": ch, "num": text[ch]})
    sorted_list.sort(reverse=True, key=sorter)
    return sorted_list