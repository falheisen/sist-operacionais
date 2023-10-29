from dataclasses import dataclass
from typing import Optional

from engine import Event

from ..jobs import Job


@dataclass
class Partition:
    start_address: int
    end_address: int
    job: Optional[Job] = None

    @property
    def size(self):
        return self.end_address - self.start_address + 1

    @property
    def is_allocated(self):
        return self._job is not None 


@dataclass
class MemoryAllocated(Event):
    job: Job


@dataclass 
class MemoryDeallocated(Event):
    job: Job


@dataclass
class MemoryAllocationFailure(Event):
    job: Job


class Memory:
    """
    Classe base para simular a gestão de memória em um sistema operacional.

    Esta classe fornece a estrutura básica e os métodos para gerir partições 
    de memória e uma lista de espera de jobs solicitando memória. As subclasses 
    devem implementar estratégias específicas de alocação de memória substituindo 
    os métodos `get_partition`

    Atributos:
        size (int): O tamanho total da memória.
        partitions (list): Uma lista de objetos Partition representando partições de memória.
        waiting (list): Uma lista de objetos Job aguardando alocação de memória.
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.partitions = [Partition(0, size - 1)]
        self.waiting: list[Job] = []

    def acquire(self, job: Job):
        if partition := self.get_partition(job):
            partition.job = job
            job.alloc_mem = partition
            yield MemoryAllocated(job=job)
        self.waiting.append(job)
        yield MemoryAllocationFailure(job=Job)
    
    def release(self, job: Job):
        for partition in self.partitions:
            if job.alloc_mem is partition:
                break
        else:
            raise Exception("could not find job partition")

    def get_partition(self, job: Job) -> Partition | None:
        raise NotImplementedError("should be overridden in subclass")

    def wake_up_next(self):
        if self.waiting and (partition := self.get_partition(self.waiting[-1])):
            job = self.waiting.pop()
            partition.job = job
            job.alloc_mem = partition



class FirstFitMemory(Memory):
    """
    Uma simulação de gestão de memória usando a estratégia de alocação First Fit.

    Na estratégia First Fit, a memória é alocada a partir da primeira partição
    encontrada que é grande o suficiente para acomodar o job.
    """

    def get_partition(self, job: Job) -> Partition | None:
        return super().get_partition(job)


class BestFitMemory(Memory):
    """
    Uma simulação de gestão de memória usando a estratégia de alocação Best Fit.

    Na estratégia Best Fit, a memória é alocada a partir da partição que,
    entre todas as partições grandes o suficiente para acomodar o job, tem o menor tamanho
    que satisfaz a solicitação de memória do job.
    """

    def get_partition(self, job: Job) -> Partition | None:
        return super().get_partition(job)


class WorstFitMemory(Memory):
    """
    Uma simulação de gestão de memória usando a estratégia de alocação Worst Fit.

    Na estratégia Worst Fit, a memória é alocada a partir da maior partição disponível.

    Herda todos os atributos e métodos da classe Memory.
    """

    def get_partition(self, job: Job) -> Partition | None:
        return super().get_partition(job)




