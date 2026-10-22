from lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv 

INPUT = "data/lab04/input.txt"
OUTPUT = "data/lab04/report.csv"
ENCODING = "utf-8"

def sorted_word_counts(freq: dict[str,int]) -> list[tuple[str,int]]:
    return sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))

def main():
    try:
        raw_text = read_text(INPUT, encoding=ENCODING)
    except FileNotFoundError:
        print(f"Ошибка: '{INPUT}' файл не найден.")
        return

    normal = normalize(raw_text)
    tokens = tokenize(normal)
    total_words = len(tokens)
    freq = count_freq(tokens)
    unique_words = len(freq)
    all_rows = sorted_word_counts(freq)
    top5 = top_n(freq, n=5)

    write_csv(all_rows, OUTPUT, header = ('word', 'count'))

    print(f'Всего слов: {total_words}')
    print(f'Уникальных слов: {unique_words}')
    print('Топ-5 слов:')
    for word, count in top5:
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()