import random

from faker import Faker


class RandomUtils:
    faker = Faker()

    @staticmethod
    def random_text():
        return RandomUtils.faker.sentence()

    @staticmethod
    def get_random_num(start_value, end_value, step):
        n = random.uniform(start_value, end_value)
        rounded_n = round(n / step) * step
        return rounded_n
