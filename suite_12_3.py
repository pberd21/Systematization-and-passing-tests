import unittest
from tests_12_3 import RunnerTest, TournamentTest

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)