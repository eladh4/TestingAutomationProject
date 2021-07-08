from http import HTTPStatus

from infra.api.rest_client import RestClient


class WorkPackagesApi(RestClient):

    # Get /api/v3/work_packages/{work_package_id}
    def get_work_package(self, work_package_id, expected_response_status_code: int = HTTPStatus.OK):
        response = self.get(path=f"/api/v3/work_packages/{work_package_id}", expected_response_status_code = expected_response_status_code)
        return response.json()

    # POST /api/v3/projects/{project_id}/work_packages
    def create_work_package(self, project_id, payload):
        response = self.post(path=f"/api/v3/projects/{project_id}/work_packages", payload=payload, expected_response_status_code=HTTPStatus.CREATED)
        return response.json()

    # PATCH /api/v3/work_packages/{work_package_id}
    def update_work_package(self, work_package_id, payload):
        response = self.patch(path=f"/api/v3/work_packages/{work_package_id}", payload=payload, expected_response_status_code=HTTPStatus.OK)
        return response.json()

    # DELETE /api/v3/work_packages/{work_package_id}
    def delete_work_package(self, work_package_id):
        response = self.delete(path=f"/api/v3/work_packages/{work_package_id}", expected_response_status_code=HTTPStatus.NO_CONTENT)

