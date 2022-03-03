import unittest
from src.task import Task
from src.task_decider import task_decider


class TestTaskDecider(unittest.TestCase):
    
    def setUp(self):
        self.dishes = Task("Wash Dishes", 10)
        self.dinner = Task("Cook Dinner", 40)
        self.windows = Task("Clean Windows", 60)

    def test_class_has_discription(self):
        self.assertEqual("Wash Dishes", self.dishes.description)
    
    def test_class_has_duration(self):
        self.assertEqual(40, self.dinner.duration)

    def test_dishes_over_dinner(self):
        self.assertEqual("Wash Dishes", task_decider("Wash Dishes", "Cook Dinner"))
    
    def test_dishes_over_dinner_flipped(self):
        self.assertEqual("Wash Dishes", task_decider("Cook Dinner", "Wash Dishes"))

    def test_dinner_over_windows(self):
        self.assertEqual("Cook Dinner", task_decider("Cook Dinner", "Clean Windows"))
    
    def test_dinner_over_windows_flipped(self):
        self.assertEqual("Cook Dinner", task_decider("Clean Windows", "Cook Dinner"))

    def test_windows_over_dishes(self):
        self.assertEqual("Clean Windows", task_decider("Clean Windows", "Wash Dishes"))
