def set_text():
    while True:
        text = input("Enter text: ")
        if len(text) > 0:
            print("text is ok")
            return text


def set_width(text):
    while True:
        try:
            width = input("Enter width: ")
            width_type = int(width)
            if width_type >= len(text) + 2 and len(text) % 2 == width_type % 2:
                return width_type
            else:
                print("Bad width")
        except ValueError:
            print("Wrong width type, try again")


def set_height():
    while True:
        try:
            height = input("Enter height: ")
            height_type = int(height)
            if height_type >= 3 and height_type % 2 != 0:
                return height_type
            else:
                print("Bad height")
        except ValueError:
            print("Wrong height type, try again")


def print_square(width, height, text):
    print("#" * width)

    if height == 3 and width == 3:
        print(f"#{text}#")

    elif width > 3 and height == 3:
        str_with_spaces = f"{' ' * (int((width - 2 - len(text)) / 2))}"
        str_with_text = f"#{str_with_spaces}{text}{str_with_spaces}#"
        print(str_with_text)

    elif width == 3 and height > 3:
        empty_lines = (int((height - 3) / 2))
        for i in range(empty_lines):
            print(f"#{' ' * (int((width - 2)))}#")
        print(f"#{text}#")
        for i in range(empty_lines):
            print(f"#{' ' * (int((width - 2)))}#")

    else:
        spaces = int((width - 2))
        empty_lines = (int((height - 3) / 2))
        for i in range(empty_lines):
            print(f"#{' ' * spaces}#")
        str_with_spaces = f"{' ' * (int((width - 2 - len(text)) / 2))}"
        str_with_text = f"#{str_with_spaces}{text}{str_with_spaces}#"
        print(str_with_text)
        for j in range(empty_lines):
            print(f"#{' ' * spaces}#")

    print("#" * width)


def square_with_text():
    text = set_text()
    width = set_width(text)
    height = set_height()
    print_square(width, height, text)


if __name__ == "__main__":
    square_with_text()
