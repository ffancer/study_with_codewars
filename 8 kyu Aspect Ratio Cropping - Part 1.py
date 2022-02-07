from typing import Tuple
from math import ceil


def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    return [ceil(y*16/9), y]



def assertion_str(x, y, actual, expected):
    return f"Testing aspect_ratio({x}, {y}) \nActual: {actual} \nExpected: {expected}\n\nError"


def test_group():
    def example_tests():
        cases = [
            # x, y, expected
            (640, 480, (854, 480)),
            (960, 720, (1280, 720)),
            (1440, 1080, (1920, 1080)),
            (1920, 1440, (2560, 1440)),
        ]

        for case in cases:
            x, y, expected = case
            actual = aspect_ratio(x, y)
            print(actual, expected, assertion_str(x, y, actual, expected))