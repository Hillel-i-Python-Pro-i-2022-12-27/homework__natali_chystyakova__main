from faker import Faker


def color_name() -> str:
    return Faker().color_name()
