from myapp.infrastructure.files_interfaces.base_interface.file_base_interface import FileBaseInterface



class FileProgressInterface(FileBaseInterface):

    def change_progress(self, procents:int)-> None:
        file_instance = self.get_interface.get(self.id)
        file_instance.progress = procents