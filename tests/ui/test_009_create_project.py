from datetime import datetime

from infra.ui.ui_utility import login, logout
from main_config import config


def test_009_create_project():

    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    project_name = f"New project! created on {timestamp}"
    project_description = f"Was created on {timestamp}"
    project_status = "ON TRACK"

    # Step 1: Login
    home_page = login(config["ui"]["username"], config["ui"]["password"])

    # Step 2: Click on "+ Project" green button (on "Home" page)
    new_project_page = home_page.click_new_project_using_plus_project_button()

    # Step 3: Type unique value for project name (on "New project" page).
    #         Name should contains letters(upper and lower), numbers, spaces, and some special characters.
    new_project_page.write_project_name(project_name)

    # Step 4: Click on "ADVANCED SETTINGS"
    new_project_page.click_on_advanced_settings()

    # Step 5: Type some text to description box
    new_project_page.write_description(project_description)

    # Step 7: Choose "ON TRACK" status
    new_project_page.select_status(project_status)

    # Step 8: Click on "Save" button and create the project
    project_overview_page = new_project_page.click_on_save_button()

    # Step 9: On "Work packages" page, top left corner, verify text on the button
    work_packages_page = project_overview_page.click_on_work_packages_link_in_menu()

    title = work_packages_page.get_project_title()
    assert title == project_name, f"Title should be: \n{project_name}, but actual is: \n{title}"

    logout()
