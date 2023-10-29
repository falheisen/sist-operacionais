from collections import deque
from ..jobs import Job
from .resource import Resource


# class CPU(Resource):
    
#     def __init__(self, concurrency: int = 1) -> None:
#         super().__init__()
#         self._concurrency = concurrency
#         self._running = deque()
#         self._waiting = deque()
    
#     def acquire(self, job: Job) -> bool:
#         if len(self._running) < self._concurrency:
#             self._running.appendleft(job)
#             return True
#         self._waiting.appendleft(job)
#         return False
    
#     def release(self, job: Job):
#         del self._executing[job]

#     def execute(self):
#         raise NotImplementedError("must be implemented in child classes")
        

# class RoundRobinCPU(CPU):

#     def execute(self):
#         job, elapsed = self._executing.pop()
#         self._executing
