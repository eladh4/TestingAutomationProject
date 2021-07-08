from datetime import datetime

from infra.api.projects_api import ProjectsApi
from main_config import config


def test_003_create_project():
    projects_api = ProjectsApi(config["base_url"])

    project_name = f"Project_{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    project_identifier = f"project_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    payload = {
        "name": project_name,
        "identifier": project_identifier
    }

    project = projects_api.create_project(payload)

    actual_name = project["name"]
    assert actual_name == project_name, f"Project name should be: \n{project_name}, but actual is: \n{actual_name}"

    actual_identifier = project["identifier"]
    assert actual_identifier == project_identifier, f"Project name should be: \n{project_identifier}, " \
                                                    f"but actual is: \n{actual_identifier}"
