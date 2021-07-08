from datetime import datetime

from infra.ui.ui_utility import login, logout
from main_config import config


def test_010_create_task():

    # Step 1: Login
    home_page = login(config["ui"]["username"], config["ui"]["password"])

    # Step 2: Click on "Select a project", and choose "TestProject1"
    home_page.click_select_a_project_button("TestProject1")

    # Step 3: Go "Work packages" page, note the number of rows displayed in the work package table
    work_packages_page = home_page.click_work_packages_button()
    num_of_work_packages_before_adding_another_one = work_packages_page.get_num_of_work_packages()

    # Step 4: Click on "+ Create" button, and select "TASK"
    new_work_package_page = work_packages_page.create_task_using_plus_create_button()

    # Step 5: Verify the text “New TASK” on top of the form that got opened on the right side
    new_work_package_page_title = new_work_package_page.get_title()

    expected_title = "TASK"
    assert new_work_package_page_title == expected_title, f"Title should be: \n{expected_title}, \
                                                          but actual is: \n{new_work_package_page_title}"

    # Step 6: Type unique strings into the subject and description boxes
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    wp_name = f"New project! created on {timestamp}"
    new_work_package_page.write_subject(wp_name)

    wp_description = f"Was created on {timestamp}"
    new_work_package_page.write_description(wp_description)

    # Step 7: Click “Save” button
    work_packages_page = new_work_package_page.click_save_button()

    # Step 8: Verify that a new row was added to the work packages table
    expected_num_of_work_packages = num_of_work_packages_before_adding_another_one  + 1
    actual_num_of_work_packages = work_packages_page.get_num_of_work_packages()
    assert expected_num_of_work_packages == actual_num_of_work_packages, \
        f"Num of work packages after adding another work package should be: \
        \n{expected_num_of_work_packages}, but actual is: {actual_num_of_work_packages}"

    # Step 9: Verify the subject and type of the last table row
    subject_last_work_package = work_packages_page.get_subject_of_work_package_in_row(actual_num_of_work_packages)
    type_last_work_package = work_packages_page.get_type_of_work_package_in_row(actual_num_of_work_packages)

    expected_subject = wp_name
    assert subject_last_work_package == expected_subject, f"Title should be \n{expected_subject}, " \
                                                        f"but actual is: \n{subject_last_work_package}"
    expected_type = expected_title
    assert type_last_work_package == expected_type, f"Title should be \n{expected_type}, " \
                                                        f"but actual is: \n{type_last_work_package}"

    logout()
