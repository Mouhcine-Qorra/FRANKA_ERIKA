from behave import given, when, then, step
import requests


@given("I access the login page")
def go_to_url(context):
    """
    call the Url using requests module
    :return:
    """
    context.myval = "myval"
    try:
        resp = requests.get(url="https://citrusframework.org/")

        # Get the code response
        StatusCode = resp.status_code

    except Exception:
        StatusCode = 0

    # Check if the Status code is between 200 and 299
    assert int(StatusCode) >= 200 and int(StatusCode) <= 299, "The Url is not Working..."

@when("I hit the login button")
def anything(context):
    pass
@then('I got an "{msg}"')
def any_other_thing(context, msg):
    print(f"the received message is ::::::::::::::::::: {msg}")
    print("context.myval ::::::::::::::::::: {}".format(context.myval))
