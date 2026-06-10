from models.task_model import create_task, get_tasks

def add_task_service(title, description, priority, user_id):
    create_task(title, description, priority, user_id)

def fetch_tasks_service(user_id):
    return get_tasks(user_id)