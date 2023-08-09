import json
from typing import Dict
from dataclasses import dataclass
from myapp.domain.files.files_descriptors.status_descriptor.status_file_descriptor import FileStatusDescriptor


@dataclass
class File:
    
    progress : str
    files : list = []
    _is_status_ok : bool = False
    status : FileStatusDescriptor = FileStatusDescriptor('_is_status_ok',True,'ok')


    def _info_status_and_progress(self)->Dict[str,str]:
        return {
            'status': self.status,
            'progress' : self.progress 
        }
    
    def _info_files(self)->Dict[str,str]:
        
        return {
            'files' : self.files
        }
    
    def out_info(self) -> str:
        out_for_json = self._info_status_and_progress()

        if self._is_status_ok:
            out_for_json.update(self._info_files())

        return json.dumps(out_for_json)
        





    



