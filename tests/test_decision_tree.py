import unittest
from src import decision_tree

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.sut = decision_tree.DecisionTree()
        pass

    def test_no_pandas(self):
        pass