from myapp.infrastructure.files_interfaces.progress_interface.file_progress_interface import FileProgressInterface
from myapp.services.core_logic.bulders.bulder_download_with_procent.bulder_download_with_procent import DownloadWithProcentBuilder
from myapp.services.core_logic.bulders.bulder_download_by_link.bulder_download_by_link import DownloadByLinkBulder
from myapp.infrastructure.clientsession.clientsession_interface import ClientSessionInterface
from myapp.services.core_logic.download_interface.download_interface import DownloadInterafce
from myapp.services.core_logic.downloader_file.downloader_file_with_procents import DownloadFileWithProcents
from myapp.services.core_logic.downloader_by_link.downloader_by_link import DownloadByLink
from myapp.services.core_logic.download_interface.download_interface import DownloadInterafce

class MakeDownloadInterafce:

    def __init__(self, file_progress_instanse : FileProgressInterface,
                       download_with_procent : DownloadWithProcentBuilder,
                       download_by_link : DownloadByLinkBulder,
                       client_session_singleton : ClientSessionInterface,
                       dowload_interface : DownloadInterafce,
                 ) -> None:
        self.file_progress_instance = file_progress_instanse
        self.download_with_procent = download_with_procent
        self.client_session_singleton = client_session_singleton
        self.download_by_link = download_by_link
        self.dowload_interface = dowload_interface

    def _make_file_progress_ready_instance(self,id:str) -> FileProgressInterface:
        return self.file_progress_instance(id)
    
    def _make_dowload_with_procent(
            self,filep_progres_with_id:FileProgressInterface
            ) -> DownloadFileWithProcents:
        return self.download_with_procent(filep_progres_with_id).ready_instanse
    
    def _make_download_by_link(
            self, ready_dowload_with_procent:DownloadFileWithProcents
            ) -> DownloadByLink:
        
        return self.download_by_link(
            self.client_session_singleton,
            ready_dowload_with_procent,

        ).ready_instanse
    
    def _make_download_interface(
            self,download_by_link_instanse:DownloadByLink
            ) -> DownloadInterafce:
        return self.dowload_interface(download_by_link_instanse)
    

    def make_ready_download_interface(self,id:str) -> DownloadInterafce:
        progress = self._make_file_progress_ready_instance(id)
        dowload_with_procents = self._make_dowload_with_procent(progress)
        download_by_link = self._make_download_by_link(dowload_with_procents)

        return self._make_download_interface(download_by_link)