from typing import Type
from pydantic import BaseModel,computed_field
from myapp.services.core_logic.download.download_with_procents import DownloadWithProcents
from myapp.infrastructure.clientsession.clientsession_interface import ClientSessionInterface
from myapp.services.core_logic.download.download_by_link import DownloadByLink
from myapp.infrastructure.files_interfaces.progress_interface.file_progress_interface import FileProgressInterface
from myapp.infrastructure.files_interfaces.status_interface.file_status_interface import FileStatusInterface


class DownloadInterface(BaseModel):
    id: str
    _status :str = 'download'

    @computed_field(return_type=Type[DownloadByLink])
    @property
    def ready_instance(self):
        file_procent_changer = FileProgressInterface(self.id)
        file_status_interface = FileStatusInterface(self.id, self._status)
        client_session = ClientSessionInterface()
        download_with_procent = DownloadWithProcents(file_procent_changer,file_status_interface)
        download_by_link = DownloadByLink(client_session,download_with_procent)
        return download_by_link
    


def get_ready_download_instance(id, 
                                download_interface:DownloadInterface = DownloadInterface
                                ) -> DownloadInterface:
    
    instance = download_interface(id=id).ready_instance
    return instance
