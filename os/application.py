
from collections import deque
from dataclasses import dataclass
from re import S
from typing import Generic, TypeVar
from engine import Application, Engine, Event
from .jobs import Job

@dataclass
class JobArrived(Event):
    job: Job

@dataclass
class JobScheduled(Event):
    job: Job

@dataclass
class JobStarted(Event):
    job: Job

@dataclass
class JobProgress(Event):
    job: Job

@dataclass
class JobDone(Event):
    job: Job

@dataclass
class MemoryAllocation(Event):
    job: Job

@dataclass
class MemoryDeallocation(Event):
    job: Job

@dataclass
class CPUAllocation(Event):
    job: Job

@dataclass
class CPUDeallocation(Event):
    job: Job


class Memory:

    def __init__(self, value: float) -> None:
        self._value = value
        self._waiting = []
        self._holding = []

    def acquire(self, job: Job):
        if (result := self._value - job.req_mem.value) >= 0:
            self._value = result
            self._holding.append(job)
            return True
        self._waiting.append(job)
        return False

    def release(self, job: Job):
        self._holding.remove(job)
        self._value += job.req_mem.value
        job.req_mem.acquired = False



class Scheduler:

    def __init__(self):
        self._waiting: list[Job] = []
        self._scheduled: 

    # def schedule(self):



@dataclass
class OSApplicationContext:
    concurrency: int
    scheduler: Scheduler
    jobs_submitted: list[Job]
    jobs_running: list[Job]


os = Application()

@os.on(JobArrived)
def handle_job_arrived(time: int, event: JobArrived, context: OSApplicationContext):
    pass


# class ResourceAllocator:

#     def acquire(self, job: Job):
#         ...

#     def release(self, job: Job):
#         ...


# class MemoryAllocator(ResourceAllocator):

#     def __init__(self, value: float) -> None:
#         super().__init__()
#         self._waiting = []
#         self._holding = []
#         self._value = value

#     def acquire(self, job: Job):
#         if (result := self._value - job.mem.value) >= 0:
#             self._value = result
#             self._holding.append(job)
#             return True
#         self._waiting.append(job)
#         return False

#     def release(self, job: Job):
#         self._holding.remove(job)
#         self._value += job.mem.value
#         job.mem.acquired = False

# class FCFSMemoryAllocator(ResourceAllocator):

#     def release(self, job: Job):
#         super().release()
#         while True:
#             if not self._waiting:
#                 break
#             if (result := self._value - self._waiting[0].mem.value) >= 0:
#                 self._value = result
#                 self._holding.append(self._waiting.pop(0))
#             else:
#                 break

# class CPUAllocator(ResourceAllocator):

#     def __init__(self, context: "OSApplicationContext", concurrency: int = 1) -> None:
#         super().__init__()
#         self._context = context
#         self._concurrency = concurrency
#         self._waiting: list[Job] = []
#         self._executing: dict[Job, int] = {}
#         self.is_busy = False

#     @property
#     def is_busy(self):
#         return len(self._executing) < self._concurrency

#     def acquire(self, job: Job):
#         if len(self._executing) < self._concurrency and job.mem.acquired:
#             self._executing[job] = 0
#             job.start = self._context.engine.time
#             job.state = "running"
#             return True
#         else:
#             self._waiting.append(job)

#     def release(self, job: Job):
#         self._executing.pop(job)
#         yield CPUDeallocation(job=job)

#     def execute(self):
#         pass

# class TimeSliceCPUAllocator(CPUAllocator):

#     def __init__(self, context: "OSApplicationContext", concurrency: int = 1, time_slice: int = 1) -> None:
#         super().__init__(context, concurrency)
#         self._time_slice = time_slice

#     def execute(self):
#         for job, executed in list(self._executing.items()):
#             if (remaining := job.cpu - executed) <= self._time_slice:
#                 # job can be completed in the time slice 
#                 self._executing.pop(job)
#                 job.state = "done"
#                 yield JobDone(job=job, delay=remaining)
#             # else:



# @os.on(JobScheduled)
# def handle_job_scheduled(event: JobScheduled, context: OSApplicationContext): 
#     ...

  

    # mem_acquired = ctx.mem.acquire(ev.job)
    # disk_acquired = ctx.mem.acquire(ev.job)

    # if all([mem_acquired,]):
    #     ctx.jobs_scheduled.append(ev.job)
    #     ctx.engine.schedule(JobScheduled(job=ev.job))

# @os.on(CPUIdle)
# def handle_cpu_idle(ev: CPUIdle, ctx: OSApplicationContext):

#     while not ctx.cpu.is_busy and ctx.jobs_waiting:
#         ctx.cpu.execute(ctx.jobs_waiting.pop())

# @os.on(MemoryDeallocation)
# def handle_resource_deallocation(event: ResourceDeallocation, context: OSApplicationContext):
#     if 




# @os.on(JobScheduled)
# def handle_job_scheduled(event: JobScheduled, context: OSApplicationContext):
#     job = context.scheduler.next()
#     yield from context.mem.acquire(job)
#     yield from context.cpu.acquire(job)

# @os.on(MemoryAllocation)
# def handle_memory_allocation(event: MemoryAllocation, context: OSApplicationContext):
#     pass

# @os.on(MemoryDeallocation)
# def handle_memory_deallocation(event: MemoryDeallocation, context: OSApplicationContext):
#     pass













    




