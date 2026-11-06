"""CLI-конвертеры данных: json2csv, csv2json, csv2xlsx."""
import argparse
import sys
from pathlib import Path

# функции из лабораторной №5 (имена модулей — как в примере из ТЗ)
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

# команда -> (функция, расширение входа, расширение выхода)
COMMANDS = {
    "json2csv": (json_to_csv, ".json", ".csv"),
    "csv2json": (csv_to_json, ".csv", ".json"),
    "csv2xlsx": (csv_to_xlsx, ".csv", ".xlsx"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Конвертеры данных JSON/CSV/XLSX (ЛР6)")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name, (_, src_ext, dst_ext) in COMMANDS.items():
        p = sub.add_parser(name, help=f"Конвертировать {src_ext} -> {dst_ext}")
        p.add_argument("--in", dest="input", required=True, help=f"Входной файл ({src_ext})")
        p.add_argument("--out", dest="output", required=True, help=f"Выходной файл ({dst_ext})")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    func, src_ext, dst_ext = COMMANDS[args.cmd]

    src, dst = Path(args.input), Path(args.output)
    if src.suffix.lower() != src_ext:
        parser.error(f"для {args.cmd} входной файл должен иметь расширение {src_ext}")
    if dst.suffix.lower() != dst_ext:
        parser.error(f"для {args.cmd} выходной файл должен иметь расширение {dst_ext}")

    try:
        if not src.is_file():
            raise FileNotFoundError(f"Входной файл не найден: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        func(str(src), str(dst))
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка данных: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Готово: {src} -> {dst}")


if __name__ == "__main__":
    main()