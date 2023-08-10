from typing import Any
from myapp.domain.files.files_descriptors.base_descriptor.base_file_descriptor import FileBaseDescriptor



class FileStatusDescriptor(FileBaseDescriptor):

    def __init__(self, attribute_to_change_with_status: str,
                 attribute_value: str,
                 status_flag: str) -> None:

        self.attribute_to_change = attribute_to_change_with_status  
        self.attribute_value = attribute_value
        self.status_flag = status_flag

    def __set__(self, instance, value: Any) -> None: 
        if value == self.status_flag:
            instance.__dict__[self.attribute_to_change] = self.attribute_value
        super().__set__(instance, value)

