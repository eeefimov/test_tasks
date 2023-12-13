def get_sides(side_name):
    while True:
        side = input(f"Enter side {side_name}: ")
        try:
            side_type = float(side)
            if side_type.is_integer() and side_type > 0:
                return int(side_type)
            elif side_type > 0:
                return side_type
            else:
                print("Value must be greater then 0")
        except ValueError:
            print("Wrong type!")


def check_sides_equal(sides_set, len_set):
    if len(sides_set) == len_set:
        print(f"triangle with {len_set} equal sides")


def check_sides_len(sides_set):
    sides_len = sorted(list(sides_set))
    print(sides_len)
    if sides_len[0] + sides_len[1] > sides_len[2]:
        print("Triangle is good")
    else:
        print("BAD")


def pythagorean_check(sides_set):
    sides_len = sorted(list(sides_set))
    if sides_len[2]**2 == sides_len[0]**2 + sides_len[1]**2:
        print("This triangle with 90 angle")


def triangle():
    letters = {"a", "b", "c"}
    sides_set = set()

    # check types
    for i in letters:
        sides_set.add(get_sides(i))
        print(sides_set)

    # check 2 or 3 equal sides
    check_sides_equal(sides_set, 1)
    check_sides_equal(sides_set, 2)

    # check normal length sides and 90
    if len(sides_set) == 3:
        check_sides_len(sides_set)
        pythagorean_check(sides_set)


if __name__ == "__main__":
    triangle()