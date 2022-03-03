
def task_decider(task1, task2):
    task_options = [task1, task2]
    if "Wash Dishes" in task_options and "Cook Dinner" in task_options:
        return "Wash Dishes"
    else:
        return "Cook Dinner"