with open('referat.txt', 'r', encoding='utf-8') as file_to_analyze:
    word_count = 0
    for line in file_to_analyze:
        if line.strip() == "":            
            continue
        word_count += len(line.strip().split(" "))
print("Количество слов - {}".format(word_count))

