import unittest
from dataclasses import dataclass

import util.input


class TestInput(unittest.TestCase):

    def test_get_input_url(self):

        @dataclass
        class TestCase:
            year: int
            day: int
            output: str

        testcases = [
            TestCase(
                2015,
                1,
                "https://adventofcode.com/2015/day/1/input",
            )
        ]

        for tc in testcases:
            output = util.input.get_input_url(tc.year, tc.day)
            self.assertEqual(tc.output, output)
