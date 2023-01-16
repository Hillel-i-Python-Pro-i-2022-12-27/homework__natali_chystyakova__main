from application import get_name_female
from application import get_color_name


def fashion_girl_says() -> None:
    print(f"Hi i'm {get_name_female()}. I dye my hair {get_color_name()}")  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == "__main__":
    fashion_girl_says()
