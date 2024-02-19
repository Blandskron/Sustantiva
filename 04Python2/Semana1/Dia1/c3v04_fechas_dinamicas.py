import unittest

from datetime import datetime
from freezegun import freeze_time


def finalizar_pandemia():

    hoy = datetime.today()
    if hoy.year > 2022:
        return True

    return False


class Test(unittest.TestCase):


    @freeze_time("2023-01-01")
    def test_finalizar_pandemia_true(self):
        print(datetime.today())
        self.assertTrue(finalizar_pandemia())

    @freeze_time("2021-01-01")
    def test_finalizar_pandemia_false(self):
        self.assertFalse(finalizar_pandemia())


if __name__ == '__main__':
    unittest.main()
