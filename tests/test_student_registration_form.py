from allure_commons.types import Severity
from demoqa_tests.pages.registration_page import RegistrationPage
import allure


@allure.tag('DemoQA')
@allure.severity(Severity.NORMAL)
@allure.label('MDN78', 'QAauto')
@allure.feature('Student Registration Form')
@allure.story('Filling certain user dates')
@allure.link('https://demoqa.com', name='Practice Form')
def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name("Ivan")
    registration_page.fill_last_name("Ivanov")
    registration_page.fill_email("Ivanov@test.com")
    registration_page.select_gender("Male")
    registration_page.fill_phone_number("1234567890")
    registration_page.fill_date_of_birth("1980", "January", "10")
    registration_page.select_hobbies("1")
    registration_page.upload_picture("picture.jpg")
    registration_page.type_subjects('Physics')
    registration_page.type_current_address("111999, St Hall avenue 34")
    registration_page.fill_state("Haryana")
    registration_page.fill_city("Karnal")
    registration_page.submit()
    #THEN
    registration_page.should_have_registered_user_with(
        "Ivan",
        "Ivanov",
        "Ivanov@test.com",
        "Male",
        "1234567890",
        "10 January,1980",
        "Physics",
        "Sports",
        "picture.jpg",
        "111999, St Hall avenue 34",
        "Haryana Karnal",
    )
    registration_page.close_submiting_form()

