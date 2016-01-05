def number(bus_stops):
    on = 0
    off = 0
    for stop in bus_stops:
        on += stop[0]
        off += stop[1]
    return on - off
