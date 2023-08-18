from myapp.infrastructure.clientsession.clientsession_interface import ClientSessionInterface
from myapp.services.core_logic.bulders.bulder_interface.base_bulder import BaseBulder
from myapp.services.core_logic.downloader_by_link.downloader_by_link import DownloadByLink
from myapp.services.core_logic.downloader_by_link.interface_dowloader_by_link import IDownloaderByLiknk
from myapp.services.core_logic.downloader_file.interface_downloader_file import IDownloaderFile


class DownloadByLinkBulder(BaseBulder):

    def __init__(self, 
                session_maker : ClientSessionInterface, 
                dowloader_with_procent : IDownloaderFile
                ) -> None:
        self.session = session_maker.make_session
        self.dowloader_with_procent_instance = dowloader_with_procent

    
    @property
    def ready_instanse(self) -> IDownloaderByLiknk:
        return DownloadByLink(self.session, self.dowloader_with_procent_instance)
    