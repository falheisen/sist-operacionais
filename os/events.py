from dataclasses import dataclass
from engine import Event
from .jobs import Job


@dataclass
class JobArrival(Event):
    id: int 
    cpu: int 
    mem: float
    
@dataclass
class JobScheduled(Event):
    job: Job

@dataclass
class JobDone(Event):
    job: Job
