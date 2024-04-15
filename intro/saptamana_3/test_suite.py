import unittest

from saptamana_3.js_alerts import TestAlerts
from saptamana_3.libraria_keys import TestKeys
from saptamana_3.test_register_page import TestRegisterPage
from saptamana_3.test_wait_for_presence import TestElementIsPresent
from saptamana_3.test_wait_for_visibility import TestElementIsVisible


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPage))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsPresent))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsVisible))

        teste_de_rulat.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPage),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsPresent),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsVisible)
            ]
        )