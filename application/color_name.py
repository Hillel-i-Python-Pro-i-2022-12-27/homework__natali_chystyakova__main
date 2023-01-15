from faker import Faker


def get_color_name() -> str:
    return Faker().color_name()
