from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test

from kitchen.models import DishType, Dish


class KitchenIndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('kitchen:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/index.html')
        self.assertContains(response, 'Dish Types')
        self.assertContains(response, 'Dishes')
        self.assertContains(response, 'Cooks')


class DishTypeListViewTest(TestCase):
    def test_dish_type_list_view(self):
        response = self.client.get(reverse('kitchen:dish-types-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dishtype_list.html')
        self.assertContains(response, 'Our dish types')


class DishTypeDetailViewTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name='Test')

    def test_dish_type_detail_view(self):
        response = self.client.get(reverse('kitchen:dish-type-detail', args=[self.dish_type.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_type_detail.html')
        self.assertContains(response, 'Our Test')


@user_passes_test(lambda x: x.is_staff)
class DishTypeCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
            is_staff=True
        )

    def test_dish_type_create_view(self):
        self.client.force_login(self.user)
        initial_count = DishType.objects.count()

        response = self.client.post(reverse('kitchen:dish-type-create'), data={'name': 'Test'})
        self.assertEqual(response.status_code, 302)

        self.assertEqual(DishType.objects.count(), initial_count + 1)

        new_dish_type = DishType.objects.get(name='Test')
        self.assertIsNotNone(new_dish_type)

    def test_dish_type_create_view_requires_staff(self):
        self.client.force_login(get_user_model().objects.create_user(
            username='non_staff_user',
            password='test_password',
            is_staff=False
        ))

        response = self.client.get(reverse('kitchen:dish-type-create'))
        self.assertEqual(response.status_code, 403)


class DishTypeListViewSearchTest(TestCase):
    def setUp(self):
        self.search_dish_type = DishType.objects.create(name='test')

    def test_dish_type_list_view_with_search(self):
        response = self.client.get(reverse('kitchen:dish-types-list'), {'dish_type': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

    def test_dish_type_list_view_with_invalid_search(self):
        response = self.client.get(reverse('kitchen:dish-types-list'), {'dish_type': 'NonExistent'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No dish types were found!')


class DishTypeDeleteViewTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name='Test')
        self.url = reverse('kitchen:dish-type-delete', args=[self.dish_type.id])

    def test_dish_type_delete_view(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)


class DishListViewTest(TestCase):
    def test_dish_list_view(self):
        response = self.client.get(reverse('kitchen:dishes-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_list.html')
        self.assertContains(response, 'List of Dishes')


@user_passes_test(lambda u: u.is_staff)
class DishCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
            is_staff=True
        )
        self.url = reverse('kitchen:dish-create')

    def test_dish_create_view(self):
        self.client.force_login(self.user)
        initial_count = Dish.objects.count()
        response = self.client.post(self.url, data={'name': 'Ramen', 'description': 'Delicious ramen', 'price': '10.99'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dish.objects.count(), initial_count + 1)


@user_passes_test(lambda u: u.is_staff)
class DishUpdateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
            is_staff=True
        )
        self.dish = Dish.objects.create(name='Tempura Udon', description='Tasty udon dish', price='15.99')
        self.url = reverse('kitchen:dish-update', args=[self.dish.id])

    def test_dish_update_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_form.html')
        self.assertContains(response, 'Update Dish')


@user_passes_test(lambda u: u.is_staff)
class DishDeleteViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            password='test_password',
            is_staff=True
        )
        self.dish = Dish.objects.create(name='Teriyaki Chicken', description='Delicious chicken dish', price='12.99')
        self.url = reverse('kitchen:dish-delete', args=[self.dish.id])

    def test_dish_delete_view(self):
        self.client.force_login(self.user)
        initial_count = Dish.objects.count()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kitchen/dish_confirm_delete.html')
        self.assertContains(response, 'Confirm Delete Dish')
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dish.objects.count(), initial_count - 1)


class SuperUserCheckMixinTest(TestCase):
    def test_superuser_check_mixin(self):
        get_user_model().objects.create_superuser(username='admin', password='adminpass')
        self.client.login(username='admin', password='adminpass')
        url = reverse('kitchen:cooks-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_common_user_check_mixin(self):
        get_user_model().objects.create_user(username='admin', password='adminpass')
        self.client.login(username='admin', password='password')
        url = reverse('kitchen:cooks-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_staff_check_mixin(self):
        get_user_model().objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.client.login(username='staff', password='password')
        url = reverse('kitchen:cooks-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
