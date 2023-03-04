from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name="Category Testing"
        )
        return super().setUp()

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        setattr(self.category, 'name', 'A' * 70)
        with self.assertRaises(ValidationError):
            self.category.full_clean()  # AQUI A VALIDAÇÃO OCORRE

    def test_category_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )
