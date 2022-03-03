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
    
    def test_dishes_over_clothes_flipped(self):
        self.assertEqual("Wash Dishes", task_decider(self.clothes, self.dishes))

    def test_dinner_over_ironing(self):
        self.assertEqual("Cook Dinner", task_decider(self.dinner, self.ironing))
    
    def test_dinner_over_ironing_flipped(self):
        self.assertEqual("Cook Dinner", task_decider(self.ironing, self.dinner))

    def test_windows_over_ironing(self):
        self.assertEqual("Clean Windows", task_decider(self.windows, self.ironing))
    
    def test_windows_over_ironing_flipped(self):
        self.assertEqual("Clean Windows", task_decider(self.ironing, self.windows))

    def test_ironing_over_clothes(self):
        self.assertEqual("Do Ironing", task_decider(self.ironing, self.clothes))
    
    def test_ironing_over_clothes_flipped(self):
        self.assertEqual("Do Ironing", task_decider(self.clothes, self.ironing))

    def test_ironing_over_dishes(self):
        self.assertEqual("Do Ironing", task_decider(self.ironing, self.dishes))
    
    def test_ironing_over_dishes_flipped(self):
        self.assertEqual("Do Ironing", task_decider(self.dishes, self.ironing))

    def test_clothes_over_dinner(self):
        self.assertEqual("Wash Clothes", task_decider(self.clothes, self.dinner))

    def test_clothes_over_dinner_flipped(self):
        self.assertEqual("Wash Clothes", task_decider(self.dinner, self.clothes))

    def test_clothes_over_windows(self):
        self.assertEqual("Wash Clothes", task_decider(self.clothes, self.windows))
    
    def test_clothes_over_windows_flipped(self):
        self.assertEqual("Wash Clothes", task_decider(self.windows, self.clothes))
