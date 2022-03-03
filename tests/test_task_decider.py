import unittest
from src.task import Task
from src.task_decider import task_decider


class TestTaskDecider(unittest.TestCase):
    
    def setUp(self):
        self.dishes = Task("Wash Dishes", 10)
        self.dinner = Task("Cook Dinner", 40)
        self.windows = Task("Clean Windows", 60)
        self.clothes = Task("Wash Clothes", 50)
        self.ironing = Task("Do Ironing", 45)

    def test_class_has_discription(self):
        self.assertEqual("Wash Dishes", self.dishes.description)
    
    def test_class_has_duration(self):
        self.assertEqual(40, self.dinner.duration)

    def test_dishes_over_dinner(self):
        self.assertEqual("Wash Dishes", task_decider(self.dishes, self.dinner))
    
    
    def test_dishes_over_dinner_flipped(self):
        self.assertEqual("Wash Dishes", task_decider(self.dinner, self.dishes))

    
    def test_dinner_over_windows(self):
        self.assertEqual("Cook Dinner", task_decider(self.dinner, self.windows))

    def test_dinner_over_windows_flipped(self):
        self.assertEqual("Cook Dinner", task_decider(self.windows, self.dinner))

    
    def test_windows_over_dishes(self):
        self.assertEqual("Clean Windows", task_decider(self.windows, self.dishes))

    
    def test_windows_over_dishes_flipped(self):
        self.assertEqual("Clean Windows", task_decider(self.dishes, self.windows))

# tests for extension

    def test_dishes_over_clothes(self):
        self.assertEqual("Wash Dishes", task_decider(self.dishes, self.clothes))