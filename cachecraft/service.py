from .parse import parse
from .core import LRU
from .extra import LFU


def run(data):
    config = parse(data)
    lru = LRU(config.capacity)
    lfu = LFU(config.capacity)
    trace = []
    a = b = 0
    for index, key in enumerate(config.keys):
        ah, ae = lru.access(key)
        bh, be = lfu.access(key)
        a += ah
        b += bh
        trace.append(
            dict(
                step=index + 1,
                key=key,
                lru_hit=ah,
                lfu_hit=bh,
                lru_evicted=ae,
                lfu_evicted=be,
                lru=lru.snapshot(),
                lfu=lfu.snapshot(),
            )
        )
    return dict(
        metrics=[
            ["Requests", len(trace)],
            ["LRU hits", a],
            ["LFU hits", b],
            ["Capacity", config.capacity],
        ],
        trace=trace,
        lru=lru.snapshot(),
        lfu=lfu.snapshot(),
        hits=[a, b],
    )
