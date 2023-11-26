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

scenarios('../Features/Demo_API.feature')

user = 0
@pytest.fixture
def base_page():
    return BasePage()
 

@given("get all resources")
def view_all_resources(base_page):
    base_page.get_request()


@when("add the resources")
def add_resources(base_page):
     global user
     user = base_page.post_request()
   


@when("update the resources")
def update_resources(base_page):
    base_page.put_request(user)


@then("delete  the resources")
def delete_resources(base_page):
    base_page.delete_request(user)
