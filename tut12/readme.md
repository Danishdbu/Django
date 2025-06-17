# Django Model Forms

## Overview
Django Model Forms are a powerful feature that simplifies creating forms directly from Django models. They automatically generate form fields based on model fields, reducing boilerplate code and ensuring consistency between database schema and form structure.

## What is a Model Form?
- A form class that is created from a Django model
- Automatically generates form fields based on model fields
- Handles validation and saving of form data to the database
- Defined using `django.forms.ModelForm` class

## Key Components
1. **ModelForm Class**: Inherits from `django.forms.ModelForm`
2. **Meta Class**: Nested class that defines model-related configurations
3. **Fields**: Automatically or explicitly defined based on model fields
4. **Widgets**: Customizable form field representations
5. **Validation**: Built-in and custom validation rules

## Step-by-Step Process to Create a Model Form

### Step 1: Define the Model
First, create a Django model in `models.py`:
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')])
```

### Step 2: Create the Model Form
In `forms.py`, define the Model Form:
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'pub_date', 'author', 'status']  # or '__all__' for all fields
```

### Step 3: Configure Meta Options
Specify model and fields in the Meta class:
```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'  # Include all model fields
        # OR
        # fields = ['title', 'content', 'pub_date']  # Specific fields
        # exclude = ['author']  # Exclude specific fields
        labels = {
            'title': 'Article Title',
            'content': 'Article Content'
        }
        help_texts = {
            'title': 'Enter a concise title for the article'
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
```

### Step 4: Use in Views
Handle the form in a view (`views.py`):
```python
from django.shortcuts import render, redirect
from .forms import ArticleForm

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data to the database
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})
```

### Step 5: Create Template
Render the form in a template (`article_form.html`):
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

### Step 6: Configure URLs
Add a URL pattern in `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_article, name='create_article'),
]
```

## Model Form Attributes
The `Meta` class supports several attributes for customization:

1. **model**:
   - Required
   - Specifies the model to base the form on
   - Example: `model = Article`

2. **fields**:
   - Specifies which model fields to include
   - Options: List of field names or `'__all__'`
   - Example: `fields = ['title', 'content']` or `fields = '__all__'`

3. **exclude**:
   - Specifies fields to exclude from the form
   - Example: `exclude = ['author', 'pub_date']`

4. **labels**:
   - Customizes field labels
   - Dictionary mapping field names to labels
   - Example: `labels = {'title': 'Article Title'}`

5. **help_texts**:
   - Provides help text for fields
   - Dictionary mapping field names to help text
   - Example: `help_texts = {'title': 'Enter a title'}`

6. **widgets**:
   - Customizes form field widgets
   - Dictionary mapping field names to widget classes
   - Example: `widgets = {'content': forms.Textarea(attrs={'rows': 5})}`

7. **field_classes**:
   - Specifies custom field classes for model fields
   - Example: `field_classes = {'title': forms.CharField}`

8. **error_messages**:
   - Customizes error messages for fields
   - Example: `error_messages = {'title': {'required': 'Title is required'}}`

9. **localized_fields**:
   - Specifies fields to be localized
   - Example: `localized_fields = ['pub_date']`

## Advanced Usage
### Custom Validation
Add custom validation by defining methods:
```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title
```

### Customizing Form Fields
Override default field types or attributes:
```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Article
        fields = '__all__'
```

### Saving with Custom Logic
Customize the save method:
```python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def save(self, commit=True):
        article = super().save(commit=False)
        article.author = self.cleaned_data['author'].upper()  # Custom logic
        if commit:
            article.save()
        return article
```

## Common Methods
1. **`form.is_valid()`**: Checks if form data is valid
2. **`form.save()`**: Saves form data to the database
3. **`form.save(commit=False)`**: Returns unsaved model instance for customization
4. **`form.as_p()`**: Renders form as HTML with `<p>` tags
5. **`form.as_table()`**: Renders form as HTML table
6. **`form.as_ul()`**: Renders form as HTML with `<ul>` tags
7. **`form.errors`**: Returns validation errors
8. **`form.cleaned_data`**: Accesses validated form data

## Best Practices
- Use `fields` or `exclude` to control form fields explicitly
- Add custom validation for business logic
- Use widgets to improve user experience
- Handle form errors gracefully in templates
- Use CSRF protection in forms
- Keep forms focused on a single model for simplicity

## Example: Complete Form with Validation
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'pub_date', 'author', 'status']
        labels = {
            'title': 'Article Title',
            'content': 'Article Content',
            'pub_date': 'Publication Date',
        }
        help_texts = {
            'title': 'Enter a descriptive title',
            'content': 'Write the article content'
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}),
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        error_messages = {
            'title': {'required': 'Please enter a title'},
            'content': {'required': 'Content cannot be empty'}
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if 'spam' in content.lower():
            raise forms.ValidationError("Content cannot contain spam")
        return content
```

## Advantages of Model Forms
- Reduces repetitive code
- Ensures consistency between model and form
- Automatic field generation
- Built-in validation based on model constraints
- Easy database integration with `save()`

## Common Issues and Solutions
1. **Issue**: Form not saving to database
   - **Solution**: Ensure `form.is_valid()` is checked before `form.save()`
2. **Issue**: Widget not rendering correctly
   - **Solution**: Verify widget attributes and CSS classes
3. **Issue**: Validation errors not showing
   - **Solution**: Include `{{ form.errors }}` in template
4. **Issue**: CSRF token missing
   - **Solution**: Add `{% csrf_token %}` in form template

## References
- Django Documentation: https://docs.djangoproject.com/en/stable/topics/forms/modelforms/
- Model Form API: https://docs.djangoproject.com/en/stable/ref/forms/models/