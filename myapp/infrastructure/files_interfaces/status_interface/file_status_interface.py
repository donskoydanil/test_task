from myapp.infrastructure.files_interfaces.base_interface.file_base_interface import FileBaseInterface

class FileStatusInterface(FileBaseInterface):

    def change_status(self, status : str) -> None:
        self.file_instance.status = status