from datetime import datetime


from infra.api.projects_api import ProjectsApi
from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def import_id_dict():
    file = open("project_id.py")
    project_id_dict = eval(file.read())
    file.close()
    return project_id_dict


def create_project_with_unique_name():
    projects_api = ProjectsApi(config["base_url"])

    project_name = f"Project_{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    project_identifier = f"project_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    payload = {
        "name": project_name,
        "project_identifier": project_identifier
    }

    project = projects_api.create_project(payload)
    return project


def create_work_package_with_unique_name():
    # Get project id of default project
    id_dict = import_id_dict()
    project_id = id_dict["project_id"]

    # Create work package
    work_packages_api = WorkPackagesApi(config["base_url"])

    work_package_subject = f"Work_package_{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

    payload = {
        "subject": work_package_subject
    }

    work_package = work_packages_api.create_work_package(project_id, payload)
    return work_package
