import arrow

def free_times(freeblock, busytimes):
  '''
  Subtract the busy times from each day's block of time
  '''
  freetimes = []
  
  if freeblock == []:
    return freetimes

  freeblockstart = freeblock['start']
  freeblockend = freeblock['end']
  
  for event in busytimes:    
      eventstart = event['start']
      eventend =event['end']
      
      # Case F
      if (eventstart <= freeblockstart) and (eventend >= freeblockend):
          return freetimes
      # Case B
      elif (eventstart <= freeblockstart) and (eventend > freeblockstart) and (eventend < freeblockend):
          freeblockstart = eventend
      # Case C
      elif (eventstart > freeblockstart) and (eventend < freeblockend):
          new_freeblock = { "start": freeblockstart, "end": eventstart }
          freetimes.append(new_freeblock)
          
          freeblockstart = eventend
      # Case D
      elif (eventstart > freeblockstart) and (eventstart < freeblockend) and (eventend >= freeblockend):
          freeblockend = eventstart
      else:
          return freetimes  
  if (freeblockstart >= freeblock['start']) and (freeblockend <= freeblock['end']):
      new_freeblock = { "start": freeblockstart, "end": freeblockend }
      freetimes.append(new_freeblock)
  else:
      return freetimes

    
  return freetimes

def available(starttime, endtime):
  '''
  Get available time block
  '''
  timeblocks = []
  
  start = arrow.get(starttime)
  end = arrow.get(endtime)
  endtime_hour = int(end.format("H"))
  endtime_min = int(end.format("m"))
  
  curdate = start
  while curdate <= end:
      temp = curdate.replace(hour=endtime_hour, minute=endtime_min)
      
      timeblocks.append(
          {
              "start": curdate.isoformat(),
              "end": temp.isoformat()
          })
      curdate = curdate.shift(days=+1)   
  return timeblocks