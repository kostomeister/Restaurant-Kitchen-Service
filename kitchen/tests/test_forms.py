from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.forms import DishTypeForm, DishForm, CookForm, DishTypeSearchForm, DishSearchForm, CookSearchForm, \
    RegistrationForm, CookUpdateForm
from kitchen.models import DishType


class DishTypeFormTest(TestCase):
    def test_dish_type_form_valid_data(self):
        form = DishTypeForm(data={'name': 'Test Course'})
        self.assertTrue(form.is_valid())

    def test_dish_type_form_no_data(self):
        form = DishTypeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


class DishFormTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name='Test Course')
        self.cook = get_user_model().objects.create(
            username='john_doe', first_name='John', last_name='Doe', years_of_experience=5
        )

    def test_dish_form_valid_data(self):
        form = DishForm(
            data={
                'name': 'Spaghetti',
                'description': 'Delicious pasta',
                'price': 10.99,
                'dish_type': self.dish_type.id,
                'cooks': [self.cook.id]}
        )
        self.assertTrue(form.is_valid())

    def test_dish_form_no_data(self):
        form = DishForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_dish_form_missing_cook(self):
        form = DishForm(data={'name': 'Pizza', 'description': 'Tasty pizza', 'price': 15.99, 'dish_type': self.dish_type.id})
        self.assertFalse(form.is_valid())
        self.assertIn('cooks', form.errors)

    def test_dish_form_invalid_price(self):
        form = DishForm(
            data={
                'name': 'Salad',
                'description': 'Fresh salad',
                'price': 'invalid_price',
                'dish_type': self.dish_type.id,
                'cooks': [self.cook.id]}
        )
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)


class CookFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            'username': 'john_doe',
            'first_name': 'John',
            'last_name': 'Doe',
            'years_of_experience': 5,
            'password1': 'securepassword',
            'password2': 'securepassword',
            'is_staff': True
        }
        self.form = CookForm(data=self.form_data)

    def test_cook_form_valid_data(self):
        self.assertTrue(self.form.is_valid())

    def test_cook_form_invalid_password1(self):
        self.form_data['password1'] = "notsecurepassword"
        form = CookForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_cook_form_invalid_password2(self):
        self.form_data['password2'] = "notsecurepassword"
        form = CookForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_cook_form_no_data(self):
        form = CookForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


class DishTypeSearchFormTest(TestCase):
    def test_dish_type_search_form_valid_data(self):
        form = DishTypeSearchForm(data={'dish_type': 'Main Course'})
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form_no_data(self):
        form = DishTypeSearchForm(data={})
        self.assertTrue(form.is_valid())


class DishSearchFormTest(TestCase):
    def test_dish_search_form_valid_data(self):
        form = DishSearchForm(data={'dish_name': 'pasta'})
        self.assertTrue(form.is_valid())

    def test_dish_search_form_empty_data(self):
        form = DishSearchForm(data={})
        self.assertTrue(form.is_valid())


class CookSearchFormTest(TestCase):
    def test_dish_search_form_valid_data(self):
        form = CookSearchForm(data={'cook_name': 'Test Cook'})
        self.assertTrue(form.is_valid())

    def test_dish_search_form_empty_data(self):
        form = DishSearchForm(data={})
        self.assertTrue(form.is_valid())


class RegistrationFormTest(TestCase):
    def test_registration_form_valid_data(self):
        form = RegistrationForm(
            data={
                "username": "test_username",
                "first_name": "Test Name",
                "last_name": "Test Surname",
                "email": "test@gmail.com",
                "password1": "testpassword1",
                "password2": "testpassword1"
            }
        )
        self.assertTrue(form.is_valid())

    def test_registration_form_not_equal_passwords(self):
        form = RegistrationForm(
            data={
                "username": "test_username",
                "first_name": "Test Name",
                "last_name": "Test Surname",
                "email": "test@gmail.com",
                "password1": "testpassword1",
                "password2": "testpassword2"
            }
        )
        self.assertFalse(form.is_valid())

    def test_registration_form_invalid_email(self):
        form = RegistrationForm(
            data={
                "username": "test_username",
                "first_name": "Test Name",
                "last_name": "Test Surname",
                "email": "testgmail.com",
                "password1": "testpassword1",
                "password2": "testpassword2"
            }
        )
        self.assertFalse(form.is_valid())

    def test_registration_form_missing_field(self):
        form = RegistrationForm(
            data={
                "username": "test_username",
                "first_name": "Test Name",
                "last_name": "Test Surname",
                "email": "test@gmail.com",
                "password1": "testpassword1",
            }
        )
        self.assertFalse(form.is_valid())


class CookUpdateFormTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username='john_doe',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            years_of_experience=5,
            password='securepassword'
        )
        self.form_data = {
            'username': 'john_doe_updated',
            'first_name': 'John_updated',
            'last_name': 'Doe_updated',
            'email': 'john_updated@example.com',
            'years_of_experience': 10
        }

    def test_cook_update_form_valid_data(self):
        form = CookUpdateForm(instance=self.cook, data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_cook_update_form_invalid_data(self):
        invalid_data = {'email': 'invalid_email'}
        form = CookUpdateForm(instance=self.cook, data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
