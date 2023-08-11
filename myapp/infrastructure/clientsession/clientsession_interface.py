import aiohttp



class ClientSessionInterface:

    
    _instanse = None

    def __new__(cls):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls)
            cls._instanse._client_session = aiohttp.ClientSession()
        return cls._instanse
        
        
    @property
    def make_session(self):
        return self._client_session
    
    async def close_session(self):
        if self._instanse._client_session:
            await self._client_session.close()