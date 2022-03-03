
from src import task


def task_decider(task1, task2):
    task_options = [task1.description, task2.description]
    if "Wash Dishes" in task_options and "Cook Dinner" in task_options:
        return "Wash Dishes"
    elif "Cook Dinner" in task_options and "Clean Windows" in task_options:
        return "Cook Dinner"
    else:
        return "Clean Windows"