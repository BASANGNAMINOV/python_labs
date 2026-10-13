# ЛР3 — Тексты и частоты слов (словарь/множество)

## Задание A — `src/lib/text.py`

### Код src/lib/text.py:
``` python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError("текст не явдяется строкой")
    if casefold:
        text=text.casefold()
    else:
        text=text.lower()
    if yo2e:
        text=text.replace("ё","е")
    return ' '.join(text.split())


def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError("текст не явдяется строкой")
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, list):
        raise TypeError("токены не являются списком")
    freq={}
    for token in tokens:
        if token in freq:
            freq[token]+=1
        else:
            freq[token]=1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sort_freq = list(freq.items())
    sort_freq.sort(key = lambda item: (-item[1], item[0]))
    return sort_freq[:n]

if __name__ == "__main__":
    print("normalize")
    for test in ["ПрИвЕт\nМИр\t", "ёжик, Ёлка", "Hello\r\nWorld", "  двойные   пробелы  "]:
        print(repr(test), "=>", repr(normalize(test)))
    print()

    print("tokenize")
    for test in ["привет мир", "hello,world!!!", "по-настоящему круто", "2025 год", "emoji 😀 не слово"]:
        print(repr(test), "=>", tokenize(test))

    print()
    print("top_n")
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    print(freq, "=>", top_n(freq, 2))
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    print(freq, "=>", top_n(freq, 2)) 
```
### Результат:

![Результат](/images/lab03/ex1,2,3.png)

## Задание B — `src/lab03/text_stats.py`
``` python 
from lib.text import normalize, tokenize, count_freq, top_n

text = input()
TABLE = 0

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
```
## Результат 
![Задание B](/images/lab03/ex4.png)

Табличный режим включается константой:

```python
TABLE = 1
```
## Результат
![N5](/images/lab03/ex5.png)