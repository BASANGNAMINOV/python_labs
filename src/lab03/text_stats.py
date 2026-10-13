from lib.text import normalize, tokenize, count_freq, top_n

text = input()
TABLE = 1

norm_text = normalize(text)
token = tokenize(norm_text)
freq = count_freq(token)
sort_freq = top_n(freq, 5)

print(f'Всего слов: {len(token)}')
print(f'Уникальных слов: {len(set(token))}')
print('Топ-5:')


if not TABLE:
    for place in sort_freq:
        print(f"{place[0]}:{place[1]}")
else:
    max_len = max([len(w[0]) for w in sort_freq] + [len("слово")])
    first_row = f"{'слово':<{max_len}} | частота"
    print(first_row)
    print("-" * (len(first_row)))

    for word in sort_freq:
        print(f"{word[0]:<{max_len}} | {word[1]}")  
