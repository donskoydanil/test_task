from myapp.infrastructure.container_interfaces.base_interface.base_container_interface import ContainerBaseInterface



class ContainerDeleteInterface(ContainerBaseInterface):

    def delete(self,id:str) -> None:
        self.container.memory.pop(id)