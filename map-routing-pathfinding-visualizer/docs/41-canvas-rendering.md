# Canvas rendering

One canvas keeps hundreds of map cells inexpensive to render. Each redraw paints the current route state, walls, and markers from the same state object.
