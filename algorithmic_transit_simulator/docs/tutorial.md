# Planning a journey

Load a network, create a router, and ask for the earliest arrival after a departure time measured in minutes after midnight.

```python
graph = load_network("data/sample_network.json")
journey = EarliestArrivalRouter(graph).route("north", "harbor", 470)
```

The returned journey contains ordered connections, aggregate fare, and final arrival time. Add a transfer buffer when operational policy requires more time between platforms.
