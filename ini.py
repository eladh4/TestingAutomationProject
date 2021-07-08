import os.path
import time

from infra.api.projects_api import ProjectsApi
from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def ini():

    # Create project with default attributes
    projects_api = ProjectsApi(config["base_url"])

    project_name = config["project_details"]["name"]
    project_description = config["project_details"]["description"]

    payload = {
        "name": project_name,
        "description": {
            "raw": project_description
        }
    }

    project = projects_api.create_project(payload)

    # Add work package to the project
    work_package_subject = config["project_details"]["work_package_subject"]

    payload = {
        "subject": work_package_subject
    }

    work_packages_api = WorkPackagesApi(config["base_url"])
    work_package = work_packages_api.create_work_package(project["id"], payload)

    # Save the id of the project and work package
    with open("project_id.py", "w") as fd:
        fd.write("{" + f"'project_id': {project['id']}, " + f"'work_package_id': {work_package['id']}" + "}")

    fd.close()

    while not os.path.isfile("project_id.py"):
        time.sleep(1)

ini()