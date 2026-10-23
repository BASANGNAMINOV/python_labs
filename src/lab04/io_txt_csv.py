import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл целиком и вернуть его содержимое одной строкой.

    По умолчанию используется UTF-8. Для другой кодировки передайте её
    явно, например: ``read_text("data/input.txt", encoding="cp1251")``.

    Если файл не найден или его содержимое нельзя декодировать в
    выбранной кодировке, возникают ``FileNotFoundError`` или
    ``UnicodeDecodeError`` соответственно. Для пустого файла вернётся ``""``.
    """
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence[object]], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Создать или перезаписать CSV-файл в кодировке UTF-8.

    Если указан ``header``, он записывается первой строкой. Все строки
    данных должны иметь одинаковую длину, а при наличии заголовка —
    совпадать по длине с ним. Иначе возникает ``ValueError``.

    Родительские директории создаются автоматически. Для пустого ``rows``
    записывается пустой файл, если заголовок не указан, или только заголовок,
    если он передан.
    """
    file_path = Path(path)
    rows = list(rows)

    if header is not None:
        length = len(header)
    elif rows:
        length = len(rows[0])
    else:
        length = None

    for row in rows:
        if len(row) != length:
            raise ValueError("Все строки CSV должны иметь одинаковую длину")

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
if __name__ == '__main__':
    print(read_text('data/lab04/input.txt'))

    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print('csv создан')