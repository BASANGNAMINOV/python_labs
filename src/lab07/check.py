import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

checks = 0  # считаем, сколько проверок прошло


def random_list():
    n = random.randint(0, 50)
    return [random.randint(-100, 100) for _ in range(n)]


def check_sorting(fn, trials=100):
    global checks
    for _ in range(trials):
        nums = random_list()
        copy = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {copy}: {result}"
        assert nums == copy, f"{fn.__name__} изменила исходный список {copy}"
        checks += 1


def check_search():
    global checks
    for _ in range(100):
        nums = random_list()
        x = random.randint(-110, 110)

        # linear_search против list.index
        if x in nums:
            expected = nums.index(x)
        else:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, f"linear_search({nums}, {x}) = {got}, ждали {expected}"
        checks += 1

        # binary_search на отсортированном списке
        s = sorted(nums)
        got = binary_search(s, x)
        if x in s:
            assert got != -1 and s[got] == x, f"binary_search({s}, {x}) = {got}"
        else:
            assert got == -1, f"binary_search({s}, {x}) = {got}, ждали -1"
        checks += 1

        # крайние элементы
        if len(s) > 0:
            for edge in (s[0], s[-1]):
                got = binary_search(s, edge)
                assert got != -1 and s[got] == edge, f"binary_search({s}, {edge}) = {got}"
                checks += 1


def check_two_sum(trials=100):
    global checks
    for _ in range(trials):
        nums = random_list()
        target = random.randint(-200, 200)
        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)
        assert (a is None) == (b is None), f"разошлись на {nums}, target={target}: {a} и {b}"
        if a is not None:
            assert a[0] < a[1] and nums[a[0]] + nums[a[1]] == target, f"brute неверна: {nums}, {a}"
            assert b[0] < b[1] and nums[b[0]] + nums[b[1]] == target, f"fast неверна: {nums}, {b}"
        checks += 1


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print(f"OK: {checks} проверок")
    