import random

from faker import Faker


class RandomUtils:
    @staticmethod
    def random_text():
        return Faker().sentence()

    @staticmethod
    def get_random_num(start_value, end_value, step):
        n = random.uniform(start_value, end_value)
        rounded_n = round(n / step) * step
        return rounded_n
    # @staticmethod
    # def random_value(min_value, max_value, step):
    #     return random.randrange(min_value, max_value, step)