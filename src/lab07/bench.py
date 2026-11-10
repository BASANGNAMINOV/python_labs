import random
import timeit
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def make_data(n):
    """Случайный список; seed одинаковый, поэтому данные повторяются."""
    random.seed(42)
    return [random.randint(0, 10**9) for _ in range(n)]


def bench():
    rows = []

    # --- сортировки ---
    for n in (1_000, 10_000, 100_000):
        data = make_data(n)  # одни и те же данные для всех сортировок

        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", t))

        if n == 100_000:
            # 10**10 шагов - это около получаса, не ждём
            for name in ("bubble_sort", "insertion_sort", "selection_sort"):
                rows.append(("sort", n, name, "> 60"))
        else:
            t = timeit.timeit(lambda: bubble_sort(data), number=1)
            rows.append(("sort", n, "bubble_sort", t))
            t = timeit.timeit(lambda: insertion_sort(data), number=1)
            rows.append(("sort", n, "insertion_sort", t))
            t = timeit.timeit(lambda: selection_sort(data), number=1)
            rows.append(("sort", n, "selection_sort", t))

    # --- поиск: 10 000 запросов к списку из 100 000 ---
    n = 100_000
    data = make_data(n)
    random.seed(1)
    # половина запросов есть в списке, половина нет
    queries = [random.choice(data) for _ in range(5_000)]
    queries += [random.randint(0, 10**9) for _ in range(5_000)]

    def run_linear():
        for x in queries:
            linear_search(data, x)

    t_linear = timeit.timeit(run_linear, number=1)
    rows.append(("search", n, "linear_search", t_linear))

    t_sort = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", n, "sort_before_binary", t_sort))

    sorted_data = sorted(data)

    def run_binary():
        for x in queries:
            binary_search(sorted_data, x)

    t_binary = timeit.timeit(run_binary, number=1)
    rows.append(("search", n, "binary_search", t_binary))

    # --- Two Sum ---
    for n in (1_000, 10_000):
        data = make_data(n)
        target = data[-2] + data[-1]  # ответ гарантированно есть
        t = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_brute", t))
        t = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        rows.append(("two_sum", n, "two_sum_fast", t))

    return rows


def fmt(value):
    if isinstance(value, float):
        return f"{value:.6f}"
    return value  # строка "> 60"


if __name__ == "__main__":
    rows = [(task, n, impl, fmt(sec)) for task, n, impl, sec in bench()]

    print(f"{'task':<10} {'n':>8}  {'impl':<20} {'seconds':>10}")
    print("-" * 52)
    for task, n, impl, sec in rows:
        print(f"{task:<10} {n:>8}  {impl:<20} {sec:>10}")

    write_csv(rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))
    print("\nСохранено в data/lab07/bench.csv")