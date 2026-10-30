from .parse import parse
from .core import analyze
from .extra import schedule


def run(data):
    tasks, workers = parse(data)
    order, early, late, children, bound = analyze(tasks)
    timeline, finish = schedule(tasks, workers)
    return dict(
        metrics=[
            ["Tasks", len(tasks)],
            ["Critical duration", bound],
            ["Scheduled duration", finish],
            ["Workers", workers],
        ],
        timeline=timeline,
        order=order,
        tasks=[
            dict(
                name=t.name,
                duration=t.duration,
                parents=t.parents,
                earliest=early[t.name],
                latest=late[t.name],
                slack=late[t.name] - early[t.name],
            )
            for t in tasks
        ],
        edges=[[p, t.name, t.duration] for t in tasks for p in t.parents],
    )
