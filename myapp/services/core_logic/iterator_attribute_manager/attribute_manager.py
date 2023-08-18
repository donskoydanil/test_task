from typing import Type,Optional
from .interface_attribute_manager import IAttributeManager
from myapp.settings.service_id_settings import SettingsId



class AttributeManager(IAttributeManager):
    


    def _make_settings_id_instanse(self,
                                attribute_container: Optional[Type[SettingsId]] = None
                                ) -> SettingsId:
        if attribute_container is None:
            attribute_container = SettingsId()
        return attribute_container

    


    def make_attrubutes(self, attribute_container:Optional[Type[SettingsId]] = None) -> None:
        container_of_attributes = self._make_settings_id_instanse(attribute_container)
        self.alphavite = container_of_attributes.alphavite
        self.end_numbers = int(container_of_attributes.upper_limit_of_numbers)



        