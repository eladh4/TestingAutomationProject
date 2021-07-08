from infra.api.utility import import_id_dict
from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_005_get_work_package():

    # Step 1: Get work package id
    id_dict = import_id_dict()
    work_package_id = id_dict["work_package_id"]

    # Step 2: Get work package
    work_packages_api = WorkPackagesApi(config["base_url"])
    response = work_packages_api.get_work_package(work_package_id)

    expected_title = config['project_details']['work_package_type']
    actual_title = response["_links"]["type"]["title"]
    assert actual_title == "Task", f"Work package_type should be: \n{expected_title}, " \
                                   f"but actual is: \n{actual_title}"

    expected_subject = config['project_details']['work_package_subject']
    actual_subject = response["subject"]
    assert actual_subject == expected_subject, f"Work package subject should be: \n{expected_subject}, " \
                                               f"but actual is: \n {actual_subject}"

