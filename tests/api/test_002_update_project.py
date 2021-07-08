from datetime import datetime

from infra.api.projects_api import ProjectsApi
from infra.api.utility import import_id_dict
from main_config import config


def test_002_update_project():

    # Step 1: Get project id
    id_dict = import_id_dict()
    project_id = id_dict["project_id"]

    # Step 2: Update project description
    new_description = f"The project description was updated on {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}."

    payload = {
        "description": {
            "raw": new_description
        }
    }

    projects_api = ProjectsApi(config["base_url"])
    project = projects_api.update_project(project_id, payload)

    actual_description = project["description"]["raw"]
    assert actual_description == new_description, f"New Project Description should be: \n{new_description}, \
                                                  but actual is: \n{actual_description}"


