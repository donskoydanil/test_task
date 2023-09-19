from typing import Type
from functools import partial
from myapp.infrastructure.clientsession.clientsession_interface import ClientSessionInterface


async def close_session(
        session_interface: Type[ClientSessionInterface]
):
    await session_interface.close_session()



close_session = partial(
    close_session,
    session_interface = ClientSessionInterface()
)
    