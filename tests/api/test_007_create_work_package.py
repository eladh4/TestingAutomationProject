from datetime import datetime

from infra.api.utility import import_id_dict
from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_007_create_work_package():

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

    actual_subject = work_package["subject"]
    assert actual_subject == work_package_subject, f"Work package subject should be: \n{work_package_subject}, " \
                                                   f"but actual is: \n{actual_subject}"
