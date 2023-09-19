from typing import Awaitable
from functools import partial
from myapp.services.utils.tasks_actions import close_tasks
from myapp.services.utils.session_actions import close_session

async def actions_in_time_shutdown(*actions:Awaitable):

    for unit in actions:
        await unit()




actions_in_time_shutdown = partial(
    actions_in_time_shutdown,
    close_tasks,
    close_session


)