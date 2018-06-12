from airflow.plugins_manager import AirflowPlugin


from plugins import blueprints
from plugins import operators



class PythonSlackPlugin(AirflowPlugin):
    name = 'do_python_slack'
    operators = [PythonSlackOperator]
    flask_blueprints = []
    hooks = []
    executors = []
    admin_views = []
    menu_links = []

    