from pages.base_page import BasePage

class LoginPage(BasePage):
    def enter_username(self, username: str):
        self.page.fill("#username", username)

    def enter_password(self, password: str):
        self.page.fill("#password", password)

    def click_login_button(self):
        self.page.click("#submit")
