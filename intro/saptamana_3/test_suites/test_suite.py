import unittest

import HtmlTestRunner
from HtmlTestRunner.result import HtmlTestResult

from saptamana_3.test_suites.js_alerts import TestAlerts
from saptamana_3.test_suites.libraria_keys import TestKeys
from saptamana_3.test_suites.test_register_page import TestRegisterPage
from saptamana_3.test_suites.test_wait_for_presence import TestElementIsPresent
from saptamana_3.test_suites.test_wait_for_visibility import TestElementIsVisible


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPage))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsPresent))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsVisible))

        # Adaugam in suita <teste_de_rulat> toate clasele de test
        # create in aceasta sesiune
        teste_de_rulat.addTests(
            [
                # intre paranteze vine exact numele clasei de test
                unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPage),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsPresent),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestElementIsVisible)
            ]
        )

        # instalam pip install html-testRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test Report PYTA14",
            report_name="Smoke test result"
        )

        runner.run(teste_de_rulat)
