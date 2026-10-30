from workbench.lab_inputs import rows, whole, names
from .models import Task


def parse(data):
    tasks = [
        Task(
            name,
            whole(duration, 1, 1000),
            tuple([] if deps == "-" else deps.split(",")),
        )
        for name, duration, deps in rows(data, "tasks", 3, 50)
    ]
    names([task.name for task in tasks])
    known = {t.name for t in tasks}
    if any(
        len(t.parents) != len(set(t.parents))
        or not set(t.parents) <= known
        or t.name in t.parents
        for t in tasks
    ):
        raise ValueError(
            "Dependencies must be distinct known tasks, excluding the task itself"
        )
    return tasks, whole(data.get("workers", 2), 1, 12)
