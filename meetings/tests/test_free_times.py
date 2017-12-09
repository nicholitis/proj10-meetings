from free_times import free_times, available
import nose


### Test free_times

def test_empty_time():
    # Empty free_times
    block = []
    busy = [{'start': '2016-01-01T09:00:00-08:00', 'end': '2016-01-01T17:00:00-08:00'}]
    free = free_times(block, busy)
    assert free == []

def test_empty_busy_times():
    # Empty busy list
    busy = []
    block = {'start': '2016-01-01T09:00:00-08:00', 'end': '2016-01-01T17:00:00-08:00'}
    free = free_times(block, busy)
    assert len(free) == 1

### Test available

def test_empty():
    #empty list
    start = "2017-01-01T00:00:00+00:00"
    end = "2016-01-01T00:00:00+00:00"
    block = available(start, end)
    assert block == []

def test_day():
    #one day
    start = "2016-01-01T00:00:00+00:00"
    end = "2016-01-01T17:00:00+00:00"
    block = available(start, end)
    assert len(block) == 1
