import requests
from config import *


def check_code_install():
	api_endpoint = '{}/api/sites/{}/check-install-code'.format(API_ENDPOINT, SITE_ID)
	response = requests.get(api_endpoint, auth=(USERNAME, API_KEY))
	if response.status_code == 417:
		print "SuperTag code is not installed."
	elif response.status_code == 200:
		print "SuperTag installed and working properly for given site."
	else:
		print "Some error occurred while checking the code install status."


if __name__ == '__main__':
	check_code_install()
