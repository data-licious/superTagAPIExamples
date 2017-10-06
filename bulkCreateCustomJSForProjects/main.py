import requests

API_USER = ''
API_TOKEN = ''
COMPANY_ID = ''


def create_tag(project_id, rapid_fire_id):
	api_endpoint = 'https://app.supert.ag/api/projects/{}/tags/template/401?error_format=new'.format(project_id)
	custom_code = """(function () {console.error('superTag license has been expired, please contact: sales@datalicious.com ')})()"""
	payload = {
		"name": "License Expired",
		"description": "",
		"fields": [{
			"field-template-id": "341",
			"value": ""
		}, {
			"field-template-id": "794",
			"value": custom_code
		}],
		"parent_id": rapid_fire_id
	}
	response = requests.post(api_endpoint, json=payload, auth=(API_USER, API_TOKEN))
	if response.status_code == 200:
		print "Added Code for Project ID: {}".format(project_id)
	else:
		print "Error adding code: {}".format(response.json().get('error'))


def create_tags():
	api_endpoint = 'https://app.supert.ag/api/companies/{}/projects'.format(COMPANY_ID)
	response = requests.get(api_endpoint, auth=(API_USER, API_TOKEN))
	if response.status_code == 200:
		response_data = response.json()
		for project in response_data.get('projects'):
			project_id = project.get('id')
			tags_api_endpoint = 'https://app.supert.ag/api/projects/{}/tags'.format(project_id)
			tags_response = requests.get(tags_api_endpoint, auth=(API_USER, API_TOKEN))
			if tags_response.status_code == 200:
				for tags in tags_response.json().get('tag_tree'):
					if tags.get('handle') == 'js.website.rapid_fire_container':
						rapid_fire_id = tags.get('id')
						create_tag(project_id, rapid_fire_id)
						break


def deploy_projects():
	api_endpoint = 'https://app.supert.ag/api/companies/{}/projects'.format(COMPANY_ID)
	response = requests.get(api_endpoint, auth=(API_USER, API_TOKEN))
	if response.status_code == 200:
		response_data = response.json()
		for project in response_data.get('projects'):
			project_id = project.get('id')
			deploy_api_endpoint = 'https://app.supert.ag/api/projects/{}/deploy'.format(project_id)
			deploy_response = requests.post(deploy_api_endpoint, auth=(API_USER, API_TOKEN))
			if deploy_response.status_code == 202 or deploy_response.status_code == 200:
				print "Scheduled Deployment for Project ID: {}".format(project_id)
			else:
				print "Error deploying project: {}".format(deploy_response.json().get('error'))


if __name__ == '__main__':
	create_tags()
	deploy_projects()
