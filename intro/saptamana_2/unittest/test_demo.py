import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Se ruleaza metoda setUp()")

    def tearDown(self):
        print("Se ruleaza metoda tearDown()")

    @unittest.skip # va sari peste acest test
    def test_1(self):
        print("Test 1")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")
        self.metoda_auxiliara()

        assert 1 + 1 == 2, "Eroare, expresia nu este adevarata"

    def test_2(self):
        print("Test 2")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")

        # assert 1 + 1 == 3, "Eroare, expresia nu este adevarata"
        self.assertEqual(1+1, 3, "Eroare, expresia nu este adevarata")

    def test_3(self):
        print("Test 3")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")
        self.metoda_auxiliara()

        self.assertTrue(3+5==10, "Text eroare")


    def test_4(self):
        print("Test 4")
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")

        lista = [1, 2, 3, 4]

        self.assertIn(8, lista, "Text eroare")

    def metoda_auxiliara(self):
        print("Se ruleaza metoda auxiliara...")