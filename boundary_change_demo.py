"""Synthetic quantity-rule illustration; no WorkBuddy or real-system execution."""


def quantity_expectation(q, upper):
    valid = type(q) is int and 1 <= q <= upper
    return "接受" if valid else "拒绝"


if __name__ == "__main__":
    print("q\t上限5\t上限3")
    for q in (0, 1, 2, 3, 4, 5, 6, 1.5):
        print(q, quantity_expectation(q, 5),
              quantity_expectation(q, 3), sep="\t")
