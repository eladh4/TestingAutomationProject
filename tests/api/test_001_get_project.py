from infra.api.projects_api import ProjectsApi
from infra.api.utility import import_id_dict
from main_config import config

basic_auth = (config["base_auth"]["user"], config["base_auth"]["password"])


def test_001_get_project():
    projects_api = ProjectsApi(config["base_url"])

    # Step 1: Get project id
    id_dict = import_id_dict()
    project_id = id_dict["project_id"]

    # Step 2:  Get project
    project = projects_api.get_project(project_id)

    expected_name = config["project_details"]["name"]
    actual_name = project["name"]
    assert actual_name == expected_name, f"Project name should be: \n'{expected_name}', but actual is: \n{actual_name}"

    expected_description = config["project_details"]["description"]
    actual_description = project["description"]["raw"]
    assert actual_description == expected_description, f"Project description should be: \n{expected_description}, \
                                                       but actual is: \n{actual_description}"



