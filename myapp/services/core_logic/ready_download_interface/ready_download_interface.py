import pathlib
from typing import Optional
from myapp.services.core_logic.maker_of_download_interface.maker_download_interface import MakeDownloadInterafce
from myapp.infrastructure.files_interfaces.progress_interface.file_progress_interface import FileProgressInterface
from myapp.services.core_logic.bulders.bulder_download_with_procent.bulder_download_with_procent import DownloadWithProcentBuilder
from myapp.services.core_logic.bulders.bulder_download_by_link.bulder_download_by_link import DownloadByLinkBulder
from myapp.infrastructure.clientsession.clientsession_interface import ClientSessionInterface
from myapp.services.core_logic.download_interface.download_interface import DownloadInterafce
from myapp.services.core_logic.download_interface.download_interface import DownloadInterafce

class ReadyDownloadInterface:

    def __init__(
            self,id:str,
            maker_of_download_interface:Optional[MakeDownloadInterafce] = None
            ) -> None:
        
        if maker_of_download_interface is None:

            maker_of_download_interface =  MakeDownloadInterafce(
                FileProgressInterface,
                DownloadWithProcentBuilder,
                DownloadByLinkBulder,
                ClientSessionInterface(),
                DownloadInterafce
            )
        
        self.ready_download_interface = \
            maker_of_download_interface.make_ready_download_interface(id)
            
    
    async def downlaod(self,url:str,path:pathlib.Path) -> None:
       await self.ready_download_interface.download(url,path)


