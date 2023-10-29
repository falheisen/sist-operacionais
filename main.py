

class Job:
    ...


class Resource:


    def __init__(self) -> None:
        self._waiters = []

    def append(self, job: Job):
        self._waiters.append(job)
    
    def remove(self, job: Job):
        self._waiters.remove(job)


class Memory:

    def __init__(self, value: float) -> None:
        self._value = value
        self._waiters = []
    
    def acquire(self, job: Job):
        if (remaining := self._value - job.mem) >= 0:
            self._value = remaining
            return True
        self._waiters.append(job)
        return False

    def release(self, job: Job):
        self._value += job.mem


class CPU:
    ...


class JobArrived:
    ...


def main():
    memory = Memory()
    cpu = CPU()

    events = [JobArrived()]
    
    while events:
        event = events.pop()
        if isinstance(event, JobArrived):
            
            memory.acquire(event.job)

        

        

