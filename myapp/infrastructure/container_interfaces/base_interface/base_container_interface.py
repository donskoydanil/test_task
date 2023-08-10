from myapp.infrastructure.container.container import Container
from typing import Type,Optional




class ContainerBaseInterface:

    def __init__(self, container:Optional[Type[Container]] = None) -> None:
        if container is None:
            container = Container()

        self.container = container