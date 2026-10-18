"""Find meeting windows across busy calendars without booking anything."""
from runtime import *

from datetime import timedelta
def process(data):
    start,end=instant(data["window_start"]),instant(data["window_end"])
    if end <= start or end-start > timedelta(days=31):
        raise ValueError("window must be positive and at most 31 days")
    duration=timedelta(minutes=integer(data["duration_minutes"],"duration_minutes",1))
    step=timedelta(minutes=integer(data.get("step_minutes",15),"step_minutes",1))
    buffer=timedelta(minutes=integer(data.get("buffer_minutes",0),"buffer_minutes"))
    intervals=[]
    for row in records(data,"busy"):
        left,right=instant(row["start"]),instant(row["end"])
        if right <= left: raise ValueError("busy interval must be positive")
        left,right=max(start,left-buffer),min(end,right+buffer)
        if right>left: intervals.append((left,right))
    merged=[]
    for left,right in sorted(intervals):
        if merged and left <= merged[-1][1]:
            merged[-1]=(merged[-1][0],max(right,merged[-1][1]))
        else: merged.append((left,right))
    slots=[]
    cursor=start
    truncated=False
    while cursor+duration <= end:
        if not any(cursor<right and cursor+duration>left for left,right in merged):
            if len(slots)==1000:
                truncated=True
                break
            slots.append({"start":cursor.isoformat(),"end":(cursor+duration).isoformat()})
        cursor+=step
    return {"slots":slots,"merged_busy":[{"start":a.isoformat(),"end":b.isoformat()} for a,b in merged],"truncated":truncated}

if __name__ == "__main__":
    sys.exit(main(process, "Find meeting windows across busy calendars without booking anything."))
