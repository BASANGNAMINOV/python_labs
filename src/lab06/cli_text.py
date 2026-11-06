"""CLI для работы с текстом: cat и stats."""
import argparse
import sys
from pathlib import Path

# функции из лабораторной №3 (при необходимости поправьте имена/модуль под свой lab03)
from src.lib.text import normalize, tokenize, count_freq, top_n


def read_text(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Входной файл не найден: {path}")
    return p.read_text(encoding="utf-8")


def cmd_cat(path: str, numbered: bool) -> None:
    text = read_text(path)
    for i, line in enumerate(text.splitlines(), start=1):
        print(f"{i:>6}\t{line}" if numbered else line)


def cmd_stats(path: str, top: int) -> None:
    text = read_text(path)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}\t{count}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом (ЛР6)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_cat = sub.add_parser("cat", help="Вывести содержимое файла построчно")
    p_cat.add_argument("--input", required=True, help="Путь к входному файлу")
    p_cat.add_argument("-n", action="store_true", help="Нумеровать строки")

    p_stats = sub.add_parser("stats", help="Частоты слов в тексте")
    p_stats.add_argument("--input", required=True, help="Путь к текстовому файлу")
    p_stats.add_argument("--top", type=int, default=5, help="Сколько слов выводить (по умолчанию 5)")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "stats" and args.top <= 0:
        parser.error("--top должен быть положительным числом")

    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            cmd_stats(args.input, args.top)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print("Ошибка: файл не в кодировке UTF-8", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()