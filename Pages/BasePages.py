import requests
import random
import json
import string

# base url:
base_url = "https://gorest.co.in"

# Auth token:
auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2ac6"

url = base_url + "/public/v2/users"
headers = {"Authorization": auth_token}
class BasePage:

    


    # get random email id:
    def generate_random_email(self):
        domain = "automation.com"
        email_length = 10
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
        email = random_string + "@" + domain
        return email


    # GET Request
    def get_request(self):
        global URL 
        URL = url
        print("get url: " + url)
        response = requests.get(url, headers=headers)
        return response
       

    def validate_get_request(self,response):
        assert response.status_code == 200
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json GET response body: ", json_str)
        print(".......GET USER IS DONE.......")
        print(".......=====================.......")

    # POST Request
    def post_request(self):    
        print("post url: " + url)
        
        data = {
            "name": "Naveen Automation",
            "email": self.generate_random_email(),
            "gender": "male",
            "status": "active"
        }
        response = requests.post(url, json=data, headers=headers)
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json POST response body: ", json_str)
        user_id = json_data["id"]
        print("user id ===>", user_id)
        assert response.status_code == 201
        assert "name" in json_data
        assert json_data["name"] == "Naveen Automation"
        print(".......POST/Create USER IS DONE.......")
        print(".......=====================.......")
        return user_id,response,response.status_code
    


    def validate_post_request(self,usr,response,status_code):
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json POST response body: ", json_str)
        user_id = json_data["id"]
        print("user id ===>", user_id)
        assert status_code == 201
        assert "name" in json_data
        assert json_data["name"] == "Naveen Automation"
        
    # PUT Request
    def put_request(self,user_id):
        url = base_url + f"/public/v2/users/{user_id}"
        print("PUT url: " + url)
      
        data = {
            "name": "Naveen Automation Labs",
            "email": self.generate_random_email(),
            "gender": "male",
            "status": "inactive"
        }
        response = requests.put(url, json=data, headers=headers)
        print(response.status_code)
        return response,response.status_code 

    def validate_put_request(self,user_id,response,status_code):
        assert status_code == 201
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print("json PUT response body: ", json_str)
        assert json_data["id"] == user_id
        assert json_data["name"] == "Naveen Automation"
        print(".......PUT/Update USER IS DONE.......")
        print(".......=====================.......")
        return response,response.status_code


    # DELETE Request
    def delete_request(self,user_id):
        url = base_url + f"/public/v2/users/{user_id}"
        print("DELETE url: " + url)
        headers = {"Authorization": auth_token}
        response = requests.delete(url, headers=headers)
        return response.status_code


    def validate_delete_request(self, status_code):
        assert status_code == 204
        print(".......DELETE USER IS DONE.......")
        print(".......=====================.......")



