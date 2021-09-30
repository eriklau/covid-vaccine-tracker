import requests
import json

API_Key = "tLBUDPpF2z-e"
Project_Token = "tf2rvLTLipDT"
Run_Token = "tLcc_OTnu-Lp"

class Data:
    def __init__(self, api_key, project_token):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{Project_Token}/last_ready_run/data', params={"api_key": API_Key})
        self.data = json.loads(response.text)
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
		}

    # def get_data(self):
	#     response = requests.get(f'https://www.parsehub.com/api/v2/projects/{Project_Token}/last_ready_run/data', params={"api_key": API_Key})
    #     self.data = json.loads(response.text)
        
    def get_total_doses(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Total Doses":
                return content['value']

    def get_reported_doses(self):
        data = self.data['total']
        
        for content in data:
            if content['name'] == "Reported Doses":
                return content['value']

        return "None"

    def get_country_data(self, country):
        data = self.data["selection1"]
        
        for content in data:
            if content['name'].lower() == country.lower():
                return content
        return "None"

if __name__ == "__main__":
    data = Data(API_Key, Project_Token)
    name = input("Enter country name: \n")
    name = name.lower()
    print(data.get_country_data(name))

