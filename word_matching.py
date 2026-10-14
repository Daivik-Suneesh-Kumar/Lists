def match_words(words):
    count = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
            list.append(word)
    print("List of words having first and last character same:",list)
    return count

list = ['abc','cfr','123','aba','1221']
count = match_words(list)
print("Number of words having first and last character same.",count)


