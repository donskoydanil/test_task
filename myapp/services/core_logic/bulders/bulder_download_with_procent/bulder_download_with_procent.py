from myapp.services.core_logic.bulders.bulder_interface.base_bulder import BaseBulder
from myapp.services.core_logic.downloader_file.downloader_file_with_procents import DownloadFileWithProcents
from myapp.infrastructure.files_interfaces.progress_interface.file_progress_interface import FileProgressInterface
from myapp.services.core_logic.downloader_file.interface_downloader_file import IDownloaderFile

class DownloadWithProcentBuilder(BaseBulder):

    def __init__(self, file_progress_interface:FileProgressInterface) -> None:
        self.file_progress_interface = file_progress_interface

    @property
    def ready_instanse(self) -> IDownloaderFile:
        return DownloadFileWithProcents(self.file_progress_interface)