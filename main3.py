import itertools

task = {
    'lesson': [1594663200, 1594666800],
    'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}
def all_events(task):
    for v in task.values():
        yield from zip(v, itertools.cycle((-1, 1)))

def presence_events(task):
    c_prev = 0
    for time, border in sorted(all_events(task)):
        c_next = c_prev + border
        if c_prev == -2 and c_next == -3:
            yield time, border
        if c_prev == -3 and c_next == -2:
            yield time, border
        c_prev = c_next

def presence(task):
    return sum(t * b for t, b in presence_events(task))

print(presence(task))