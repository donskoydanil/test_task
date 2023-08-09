from myapp.infrastructure.container.container import Container
from typing import Type




class ContainerBaseInterface:

    def __init__(self, container:Type[Container]) -> None:
        if container is None:
            container = Container()

        self.container = container