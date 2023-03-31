class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Назва',
            'description': 'Опис'
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'description', 'category']
        labels = {
            'name': 'Назва',
            'description': 'Опис',
            'category': 'Категорія'
        }
urlpatterns = [
    # ...
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/<int:pk>/edit/', views
