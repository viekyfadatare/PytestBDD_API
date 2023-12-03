import pytest
import requests
import random
import json
import string

from pytest_bdd import scenarios
import time
from pathlib import Path
from pytest_bdd import given, when, then, scenario, scenarios

from Pages.BasePages import BasePage
from Logger import get_logger

scenarios("../Features/Demo_API.feature")

user = 0
post_response = None
post_status_code = None

log = get_logger()

@pytest.fixture
def base_page():
    return BasePage()


 
@given("I initiated /api/user get API")
def view_all_resources(base_page):
    log.info("In given method")
    global get_response 
    get_response = base_page.get_request()


@then("I validate /api/user get response")    
def valiadte_get(base_page):
    log.info("I valiadate user get")
    base_page.validate_get_request(get_response)


@given("I initiated /api/users post API")
def add_resources(base_page):
     log.info("Add resource ")
     global user,post_response,post_status_code
     user,post_response,post_status_code = base_page.post_request()
     print("add resourse",user,post_response,post_status_code)
   

@then("I validate /api/users post response")
def validate_post(base_page):  
    log.info("Validfate Add resource ")
    print(user,post_response,post_status_code)
    base_page.validate_post_request(user,post_response,post_status_code)


@given("I initiated /api/users/2 put API")
def update_resources(base_page):
    log.info("Put resource ")
    global put_response,put_status_code
    put_response,put_status_code=base_page.put_request(user)



@then("I validate /api/users/2 put response")
def validate_put(base_page):
    log.info("Validate Put resource ")
    base_page.validate_put_request(user,post_response,post_status_code)

@given("I initiated /api/users/2 delete API")
def delete_resourcse(base_page):
    log.info("Delete resource ")
    global delete_status_code
    delete_status_code=base_page.delete_request(user)

@then("I validate /api/users/2 delete response")
def validate_delete(base_page):
    log.info("Valiadte Delete resource ")
    base_page.validate_delete_request(delete_status_code)    
