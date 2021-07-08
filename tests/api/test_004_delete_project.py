import time

from infra.api.projects_api import ProjectsApi
from infra.api.utility import create_project_with_unique_name
from main_config import config


def test_004_delete_project():

    # Step 1: Create new project
    project = create_project_with_unique_name()

    # Step 2: Delete project by id
    project_id = project["id"]
    projects_api = ProjectsApi(config["base_url"])
    projects_api.delete_project(project_id)

    # Step 3: Verify the project was deleted by try to get it
    time_to_sleep = 7
    print(f"Sleep {time_to_sleep} seconds before validating deletion")
    time.sleep(time_to_sleep)
    projects_api.get_project(project_id, expected_response_status_code=404)
