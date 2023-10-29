
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, Literal, TypeVar


if TYPE_CHECKING:
    from .application import OSApplicationContext
    from .resources.memory import Partition



@dataclass
class Job:
    id: int 
    
    arrival: int
    start: int | None = None
    end: int | None = None

    state: Literal["scheduled", "running", "halted", "cancelled", "done"] = "scheduled"

    req_cpu_time: int
    req_mem: int

    alloc_cpu_time: int | None = None
    alloc_mem: Partition | None = None




    # disk: float = 0
    # disk_acquired: bool = False

    # io: int = 0
    # io_acquired: bool = False



class JobScheduler:

    def __init__(self, context: "OSApplicationContext") -> None:
        self._context = context
    
    def next(self) -> Job:
        raise NotImplementedError("must be implemented in child classes")

    def schedule(self, job: Job):
        raise NotImplementedError("must be implemented in child classes")
        

class FIFOJobScheduler(JobScheduler):

    def schedule(self, job: Job):
        # if 


        return super().schedule(job)

