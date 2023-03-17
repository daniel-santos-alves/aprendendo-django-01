import os

from django.urls import reverse

from recipes.tests.test_recipe_base import RecipeTestBase
from utils.pagination import make_pagination_range

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


class paginationTest(RecipeTestBase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501
        # current page = 1 - qty page = 4 - middle page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # current page = 2 - qty page = 4 - middle page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        # current page = 3 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        # current page = 4 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        # current page = 10 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        # current page = 12 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        # current page = 18 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # current page = 19 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # current page = 20 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        # current page = 21 - qty page = 4 - middle page = 2
        # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_make_pagination_home_qty_recipes_is_12(self):

        recipe1 = self.make_recipe(  # noqa: F841
            slug='one', title='This is recipe one',
            author_data={'username': 'one'},
        )
        recipe2 = self.make_recipe(  # noqa: F841
            slug='two', title='This is recipe two',
            author_data={'username': 'two'},
        )
        recipe3 = self.make_recipe(  # noqa: F841
            slug='three', title='This is recipe three',
            author_data={'username': 'three'},
        )
        recipe4 = self.make_recipe(  # noqa: F841
            slug='four', title='This is recipe four',
            author_data={'username': 'four'},
        )
        recipe5 = self.make_recipe(  # noqa: F841
            slug='five', title='This is recipe five',
            author_data={'username': 'five'},
        )
        recipe6 = self.make_recipe(  # noqa: F841
            slug='six', title='This is recipe six',
            author_data={'username': 'six'},
        )
        recipe7 = self.make_recipe(  # noqa: F841
            slug='seven', title='This is recipe seven',
            author_data={'username': 'seven'},
        )
        recipe8 = self.make_recipe(  # noqa: F841
            slug='eight', title='This is recipe eight',
            author_data={'username': 'eight'},
        )
        recipe9 = self.make_recipe(  # noqa: F841
            slug='nine', title='This is recipe nine',
            author_data={'username': 'nine'},
        )
        recipe10 = self.make_recipe(  # noqa: F841
            slug='ten', title='This is recipe ten',
            author_data={'username': 'ten'},
        )
        recipe11 = self.make_recipe(  # noqa: F841
            slug='eleven', title='This is recipe eleven',
            author_data={'username': 'eleven'},
        )
        recipe12 = self.make_recipe(  # noqa: F841
            slug='twelve', title='This is recipe twelve',
            author_data={'username': 'twelve'},
        )

        url = reverse('recipes:home')
        response = self.client.get(f'{url}?page={1}')
        qty_recipes = len(response.context['recipes'])

        self.assertEqual(qty_recipes, PER_PAGE)

    def test_make_pagination_home_qty_recipes_is_12_with_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'
        title3 = 'This is recipe three'
        title4 = 'This is recipe four'
        title5 = 'This is recipe five'
        title6 = 'This is recipe six'
        title7 = 'This is recipe seven'
        title8 = 'This is recipe eight'
        title9 = 'This is recipe nine'
        title10 = 'This is recipe ten'
        title11 = 'This is recipe eleven'
        title12 = 'This is recipe twelve'

        recipe1 = self.make_recipe(  # noqa: F841
            slug='one', title=title1,
            author_data={'username': 'one'},
        )
        recipe2 = self.make_recipe(  # noqa: F841
            slug='two', title=title2,
            author_data={'username': 'two'},
        )
        recipe3 = self.make_recipe(  # noqa: F841
            slug='three', title=title3,
            author_data={'username': 'three'},
        )
        recipe4 = self.make_recipe(  # noqa: F841
            slug='four', title=title4,
            author_data={'username': 'four'},
        )
        recipe5 = self.make_recipe(  # noqa: F841
            slug='five', title=title5,
            author_data={'username': 'five'},
        )
        recipe6 = self.make_recipe(  # noqa: F841
            slug='six', title=title6,
            author_data={'username': 'six'},
        )
        recipe7 = self.make_recipe(  # noqa: F841
            slug='seven', title=title7,
            author_data={'username': 'seven'},
        )
        recipe8 = self.make_recipe(  # noqa: F841
            slug='eight', title=title8,
            author_data={'username': 'eight'},
        )
        recipe9 = self.make_recipe(  # noqa: F841
            slug='nine', title=title9,
            author_data={'username': 'nine'},
        )
        recipe10 = self.make_recipe(  # noqa: F841
            slug='ten', title=title10,
            author_data={'username': 'ten'},
        )
        recipe11 = self.make_recipe(  # noqa: F841
            slug='eleven', title=title11,
            author_data={'username': 'eleven'},
        )
        recipe12 = self.make_recipe(  # noqa: F841
            slug='twelve', title=title12,
            author_data={'username': 'twelve'},
        )

        url = reverse('recipes:home')
        response = self.client.get(f'{url}?page={1}')
        context_page_home = response.content.decode('utf-8')

        self.assertIn(title1, context_page_home)
        self.assertIn(title2, context_page_home)
        self.assertIn(title3, context_page_home)
        self.assertIn(title4, context_page_home)
        self.assertIn(title5, context_page_home)
        self.assertIn(title6, context_page_home)
        self.assertIn(title7, context_page_home)
        self.assertIn(title8, context_page_home)
        self.assertIn(title9, context_page_home)
        self.assertIn(title10, context_page_home)
        self.assertIn(title11, context_page_home)
        self.assertIn(title12, context_page_home)
