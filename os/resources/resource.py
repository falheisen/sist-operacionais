




class Resource:
    
    def acquire(self, *args, **kwargs) -> bool:
        ...

    def release(self, *args, **kwargs) -> None:
        ...
