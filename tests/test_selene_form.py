import allure
from allure_commons.types import Severity

from pages.registration_page import RegistrationPage


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.feature('Автотесты')
@allure.story('Форма')
@allure.title('Заполнение')
def test_user_can_send_form():
    registration_page = RegistrationPage()
    (
        (
            registration_page.open()
            .fill_first_name('Masha')
            .fill_last_name('Maria')
            .fill_email('mama@mail.ru')
            .fill_gender('2')
            .fill_phone_number('7987654543')
            .fill_date_of_birth('2022', 'July', '12')
            .fill_subjects('Hindi')
            .fill_hobbies('1')
            .upload_picture('picture.jpg')
            .fill_address('Address')
            .fill_state('NCR')
            .fill_city('Delhi')

            .submit()
            .should_registered_user_with(
                'Masha Maria',
                'mama@mail.ru',
                'Female',
                '7987654543',
                '12 July,2022',
                'Hindi',
                'Sports',
                'picture.jpg',
                'Address',
                'NCR Delhi',
            )
        )
    )
