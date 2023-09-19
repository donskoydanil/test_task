from myapp.services.utils.app_actions import actions_in_time_shutdown
from myapp.services.utils.tasks_actions import close_tasks
from myapp.services.utils.session_actions import close_session

async def close_app(application):
    await actions_in_time_shutdown(close_tasks,close_session)