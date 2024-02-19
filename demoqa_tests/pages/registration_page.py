import allure
from selene import browser, have, be
from selene.core import command

from demoqa_tests import resource


class RegistrationPage:

    @allure.step('Open maim page')
    def open(self):
        browser.open("/automation-practice-form")
        # удаление рекламы - предусловие тестового сценария
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    @allure.step('Input first name {value}')
    def fill_first_name(self, value):
        browser.element("#firstName").should(be.blank).send_keys(value)

    @allure.step('Input last name {value}')
    def fill_last_name(self, value):
        browser.element("#lastName").should(be.blank).send_keys(value)

    @allure.step('Input e-mail {value}')
    def fill_email(self, value):
        browser.element("#userEmail").should(be.blank).send_keys(value)

    @allure.step('Select gender {value}')
    def select_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()

    @allure.step('Input phone number {value}')
    def fill_phone_number(self, value):
        browser.element("#userNumber").should(be.blank).send_keys(value)

    @allure.step('Fill date of birth {year} {month} {day}')
    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(".react-datepicker__month-select").send_keys(month)
        browser.element(f".react-datepicker__day--0{day}").click()

    @allure.step('Input subjects {value}')
    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    @allure.step('Select hobbies {value}')
    def select_hobbies(self, value):
        browser.element("[for=hobbies-checkbox-2]").perform(command.js.scroll_into_view)
        browser.all("[type=checkbox]").element_by(have.value(value)).element("..").click()

    @allure.step('Upload picture with name {value}')
    def upload_picture(self, value):
        browser.element("#uploadPicture").send_keys(resource.path(value))

    @allure.step('Input current address {value}')
    def type_current_address(self, value):
        browser.element("#currentAddress").send_keys(value)

    @allure.step('Select state {state}')
    def fill_state(self, state):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(state)
        ).click()

    @allure.step('Select city {city}')
    def fill_city(self, city):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(city)
        ).click()

    @allure.step('Confirm form')
    def submit(self):
        browser.element("#submit").submit()

    @allure.step('Checking registration form')
    def should_have_registered_user_with(
            self,
            first_name,
            last_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            state_city,
    ):
        browser.element(".table").all("td:nth-child(2)").should(
            have.exact_texts(
                f"{first_name} {last_name}",
                email,
                gender,
                mobile,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_city,
            )
        )

    @allure.step('Close modal window')
    def close_submiting_form(self):
        browser.element("#closeLargeModal").double_click()
