import arrow


def busy_times(things, startOfRange, endOfRange):
  startdate = arrow.get(startOfRange).date()
  enddate = arrow.get(endOfRange).date()
  starttime = arrow.get(startOfRange).time()
  endtime = arrow.get(endOfRange).time()

  timeslots = []

  if things == []:
    return "no events"

  else:
    for entry in things:
      #busy time
      if "transparency" not in entry:
        #all day event
        if "date" in entry["start"]:
          summary = entry["summary"]
          start = entry["start"]["date"] + "00:00:00" + startOfRange[19:]
          end = entry["end"]["date"] + "23:59:00" + endOfRange[19:]
          event_begin_date = arrow.get(start).date()
          event_begin_time = arrow.get(start).time()
          event_end_date = arrow.get(end).date()
          event_end_time = arrow.get(end).time()
        else:
          #normal event
          summary = entry["summary"]
          start = entry["start"]["dateTime"]
          end = entry["end"]["dateTime"]
          event_begin_date = arrow.get(start).date()
          event_begin_time = arrow.get(start).time()
          event_end_date = arrow.get(end).date()
          event_end_time = arrow.get(end).time()
        
        #event is either directly in range or on either edges
        inRange = (event_begin_date >= startdate) and (event_end_date <= enddate) and (event_begin_time >= starttime) and (event_end_time <= endtime)
        edgeRange = (event_begin_date >= startdate) and (event_end_date <= enddate) and (event_begin_time < starttime) and ((event_end_time >= endtime) or (event_end_time <= endtime)) and (event_end_time > starttime)
        otherEdgeRange = (event_begin_date >= startdate) and (event_end_date <= enddate) and (event_begin_time < endtime) and ((event_end_time >= endtime) or (event_end_time <= endtime)) and (event_end_time > endtime)
        
        if (inRange or edgeRange or otherEdgeRange):
          event = {"summary":summary, "start":start, "end":end }
          timeslots.append(event)

  return timeslots