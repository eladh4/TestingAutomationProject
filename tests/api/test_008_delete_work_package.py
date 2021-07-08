import time
from datetime import datetime

from infra.api.utility import import_id_dict, create_work_package_with_unique_name
from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_008_delete_work_package():

    # Step 1: Create work package
    work_package = create_work_package_with_unique_name()

    # Step 2: Delete the newly created work package
    work_packages_api = WorkPackagesApi(config["base_url"])
    work_packages_api.delete_work_package(work_package["id"])

    # Step 3: Verify the work package was deleted by try to get it
    time_to_sleep = 7
    print(f"Sleep {time_to_sleep} seconds before validating deletion")
    time.sleep(time_to_sleep)
    work_packages_api.get_work_package(work_package["id"], expected_response_status_code=404)
