from datetime import datetime

from infra.api.utility import import_id_dict
from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_006_update_work_package():

    # Step 1: Get work package id
    id_dict = import_id_dict()
    work_package_id = id_dict["work_package_id"]

    # Step 2: Get work package
    work_packages_api = WorkPackagesApi(config["base_url"])
    work_package = work_packages_api.get_work_package(work_package_id)

    # Step 3: Update work package description
    new_description = f"Update on Auto Project {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    payload = {
        "lockVersion": work_package["lockVersion"],
        "description": {
            "raw": new_description
        }
    }

    response = work_packages_api.update_work_package(work_package_id, payload)
    actual_description = response["description"]["raw"]

    assert actual_description == new_description, f"Work package description should be: \n{new_description}, " \
                                                  f"but actual is: \n{actual_description}"
