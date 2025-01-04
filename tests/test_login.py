import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [("student", "Passworld123")])
def test_login(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate("https://practicetestautomation.com/practice-test-login/")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert page.url == "https://practicetestautomation.com/practice-test-login/"
