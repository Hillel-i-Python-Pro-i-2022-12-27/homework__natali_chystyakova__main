from faker import Faker


def get_name_female() -> str:
    return Faker().name_female()
