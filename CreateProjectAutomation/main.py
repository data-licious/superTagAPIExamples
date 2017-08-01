import requests
from config import *


def create_project():
	api_endpoint = '{}/api/companies/{}/project'.format(API_ENDPOINT, COMPANY_ID)
	parameters = {
		'name': PROJECT_NAME,
		'async': ASYNC_JS
	}
	response = requests.post(api_endpoint, json=parameters, auth=(USERNAME, API_KEY))
	if response.status_code == 200 or response.status_code == 201:
		print "Project Created"
		return response.json().get('id')
	else:
		raise Exception('Project Creation Failed. {}'.format(response.json().get('message'))) 


def copy_project(project_id):
	if not project_id:
		raise Exception("Project ID Empty!")
	api_endpoint = '{}/api/tags/{}/copy-to-project/{}'.format(API_ENDPOINT, CONTAINER_ID_TO_COPY, project_id)
	response = requests.post(api_endpoint, auth=(USERNAME, API_KEY))
	if response.status_code == 200:
		print "Tags copied."
	else:
		raise Exception('Copying Tag Failed. {}'.format(response.json().get('message'))) 


def main():
	project_id = create_project()
	copy_project(project_id)


if __name__ == '__main__':
	main()
