
# **What is Django ORM?**
Django ORM is a layer between your Python code and the database. It maps Python classes (models) to database tables, class instances to rows, and attributes to columns. This abstraction allows you to work with databases like SQLite, PostgreSQL, MySQL, or Oracle without writing SQL queries directly.

### **Key Features of Django ORM**
- **Database Agnostic**: Write code once, and it works with multiple databases.
- **Model-Based**: Define database schema using Python classes.
- **QuerySet API**: Perform database operations using Python methods.
- **Migration System**: Automatically generate and apply database schema changes.
- **Relationships**: Support for one-to-one, one-to-many, and many-to-many relationships.

---

## **Topics Covered**
1. **Defining Models**
2. **Database Migrations**
3. **CRUD Operations (Create, Read, Update, Delete)**
4. **QuerySet API**
5. **Relationships (ForeignKey, OneToOneField, ManyToManyField)**
6. **Aggregations and Annotations**
7. **Raw SQL Queries**
8. **Database Transactions**
9. **Indexes and Constraints**
10. **Database Configuration**

---

## **1. Defining Models**
Models are Python classes that represent database tables. Each model is a subclass of `django.db.models.Model`, and its attributes represent table columns.

### **Syntax**
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'authors'  # Custom table name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'
```

### **Explanation**
- **Fields**: `CharField`, `EmailField`, `DateTimeField`, `DateField`, `ForeignKey` are field types mapping to database column types (e.g., `VARCHAR`, `DATE`).
- **`max_length`**: Specifies the maximum length for string fields.
- **`unique=True`**: Enforces uniqueness at the database level.
- **`auto_now_add=True`**: Sets the field to the current timestamp when the object is created.
- **`ForeignKey`**: Defines a many-to-one relationship (explained later).
- **`Meta` class**: Configures table metadata, like the table name.
- **Database Mapping**: The `Author` model creates a table `authors` with columns `id` (auto-generated primary key), `name`, `email`, and `created_at`.

---

## **2. Database Migrations**
Migrations translate model changes into database schema changes. Django tracks model changes and generates SQL to apply them.

### **Steps**
1. **Create Migrations**:
   ```bash
   python manage.py makemigrations
   ```
   This generates migration files in the `migrations/` directory based on model changes.

2. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```
   This runs the SQL to create/update tables in the database.

### **Example Migration File**
```python
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'db_table': 'authors'},
        ),
    ]
```

### **Explanation**
- **Migration File**: Defines operations like `CreateModel` to create the `authors` table.
- **Fields**: Maps Python field types to SQL column types (e.g., `CharField` → `VARCHAR`).
- **Dependencies**: Tracks relationships between migrations.
- **`migrate`**: Executes the SQL to create the table in the database.


---

## **1. Overview of Django Fields and Data Types**

Django provides a variety of field types in the `django.db.models` module to represent different kinds of data. Each field type maps to a specific database column type, which may vary slightly depending on the database backend (e.g., PostgreSQL, MySQL, SQLite). Below is a comprehensive list of Django field types, their purposes, and their database mappings.

---

## **2. Django Field Types and Database Mappings**

Below is a detailed list of Django’s field types, their purpose, the corresponding database data types, and examples. I’ll also include the SQL equivalent for clarity (based on PostgreSQL, as it’s a common backend).

### **Basic Field Types**

1. **CharField**
   - **Purpose**: Stores fixed-length strings (e.g., names, titles).
   - **Database Data Type**: `VARCHAR(max_length)` or `CHAR(max_length)` (depending on the database).
   - **Required Parameter**:
     - `max_length`: Maximum number of characters (e.g., `max_length=100`).
   - **Example**:
     ```python
     name = models.CharField(max_length=100)
     ```
     **SQL Equivalent**: `name VARCHAR(100)`

2. **TextField**
   - **Purpose**: Stores large amounts of text (e.g., descriptions, articles).
   - **Database Data Type**: `TEXT`.
   - **Example**:
     ```python
     description = models.TextField()
     ```
     **SQL Equivalent**: `description TEXT`

3. **IntegerField**
   - **Purpose**: Stores integer values (e.g., counts, quantities).
   - **Database Data Type**: `INTEGER`.
   - **Example**:
     ```python
     quantity = models.IntegerField()
     ```
     **SQL Equivalent**: `quantity INTEGER`

4. **BigIntegerField**
   - **Purpose**: Stores large integer values.
   - **Database Data Type**: `BIGINT`.
   - **Example**:
     ```python
     big_number = models.BigIntegerField()
     ```
     **SQL Equivalent**: `big_number BIGINT`

5. **SmallIntegerField**
   - **Purpose**: Stores small integer values.
   - **Database Data Type**: `SMALLINT`.
   - **Example**:
     ```python
     small_number = models.SmallIntegerField()
     ```
     **SQL Equivalent**: `small_number SMALLINT`

6. **PositiveIntegerField**
   - **Purpose**: Stores non-negative integers (0 or positive).
   - **Database Data Type**: `INTEGER` with a check constraint for non-negativity.
   - **Example**:
     ```python
     age = models.PositiveIntegerField()
     ```
     **SQL Equivalent**: `age INTEGER CHECK (age >= 0)`

7. **PositiveSmallIntegerField**
   - **Purpose**: Stores small non-negative integers.
   - **Database Data Type**: `SMALLINT` with a check constraint.
   - **Example**:
     ```python
     score = models.PositiveSmallIntegerField()
     ```
     **SQL Equivalent**: `score SMALLINT CHECK (score >= 0)`

8. **FloatField**
   - **Purpose**: Stores floating-point numbers.
   - **Database Data Type**: `DOUBLE PRECISION` or `FLOAT`.
   - **Example**:
     ```python
     price = models.FloatField()
     ```
     **SQL Equivalent**: `price DOUBLE PRECISION`

9. **DecimalField**
   - **Purpose**: Stores fixed-point decimal numbers (e.g., currency).
   - **Database Data Type**: `DECIMAL(max_digits, decimal_places)` or `NUMERIC`.
   - **Required Parameters**:
     - `max_digits`: Total number of digits.
     - `decimal_places`: Number of decimal places.
   - **Example**:
     ```python
     amount = models.DecimalField(max_digits=10, decimal_places=2)
     ```
     **SQL Equivalent**: `amount DECIMAL(10, 2)`

10. **BooleanField**
    - **Purpose**: Stores `True` or `False` values.
    - **Database Data Type**: `BOOLEAN`.
    - **Example**:
      ```python
      is_active = models.BooleanField()
      ```
      **SQL Equivalent**: `is_active BOOLEAN`

11. **NullBooleanField**
    - **Purpose**: Stores `True`, `False`, or `NULL` (deprecated; use `BooleanField(null=True)` instead).
    - **Database Data Type**: `BOOLEAN` with nullable support.
    - **Example**:
      ```python
      is_verified = models.BooleanField(null=True)
      ```
      **SQL Equivalent**: `is_verified BOOLEAN NULL`

12. **DateField**
    - **Purpose**: Stores a date (e.g., `2025-06-12`).
    - **Database Data Type**: `DATE`.
    - **Example**:
      ```python
      birth_date = models.DateField()
      ```
      **SQL Equivalent**: `birth_date DATE`

13. **DateTimeField**
    - **Purpose**: Stores a date and time (e.g., `2025-06-12 16:40:00`).
    - **Database Data Type**: `TIMESTAMP` or `DATETIME`.
    - **Example**:
      ```python
      created_at = models.DateTimeField()
      ```
      **SQL Equivalent**: `created_at TIMESTAMP`

14. **TimeField**
    - **Purpose**: Stores a time (e.g., `16:40:00`).
    - **Database Data Type**: `TIME`.
    - **Example**:
      ```python
      start_time = models.TimeField()
      ```
      **SQL Equivalent**: `start_time TIME`

15. **DurationField**
    - **Purpose**: Stores a time interval (e.g., `1 day, 2 hours`).
    - **Database Data Type**: `INTERVAL` (PostgreSQL) or `BIGINT` (other databases, storing microseconds).
    - **Example**:
      ```python
      duration = models.DurationField()
      ```
      **SQL Equivalent**: `duration INTERVAL` (PostgreSQL)

16. **EmailField**
    - **Purpose**: Stores email addresses (like `CharField` with validation).
    - **Database Data Type**: `VARCHAR(max_length)` (default `max_length=254`).
    - **Example**:
      ```python
      email = models.EmailField()
      ```
      **SQL Equivalent**: `email VARCHAR(254)`

17. **URLField**
    - **Purpose**: Stores URLs with validation.
    - **Database Data Type**: `VARCHAR(max_length)` (default `max_length=200`).
    - **Example**:
      ```python
      website = models.URLField()
      ```
      **SQL Equivalent**: `website VARCHAR(200)`

18. **SlugField**
    - **Purpose**: Stores URL-friendly strings (e.g., `my-post-title`).
    - **Database Data Type**: `VARCHAR(max_length)` (default `max_length=50`).
    - **Example**:
      ```python
      slug = models.SlugField(max_length=100)
      ```
      **SQL Equivalent**: `slug VARCHAR(100)`

19. **UUIDField**
    - **Purpose**: Stores a universally unique identifier (UUID).
    - **Database Data Type**: `UUID` (PostgreSQL) or `CHAR(32)` (other databases).
    - **Example**:
      ```python
      uuid = models.UUIDField()
      ```
      **SQL Equivalent**: `uuid UUID` (PostgreSQL)

20. **FileField**
    - **Purpose**: Stores file uploads (path to the file).
    - **Database Data Type**: `VARCHAR(max_length)` (default `max_length=100`).
    - **Required Parameter** (optional): `upload_to`: Directory path for file storage.
    - **Example**:
      ```python
      document = models.FileField(upload_to='documents/')
      ```
      **SQL Equivalent**: `document VARCHAR(100)`

21. **ImageField**
    - **Purpose**: Stores image uploads (requires Pillow library).
    - **Database Data Type**: `VARCHAR(max_length)` (default `max_length=100`).
    - **Required Parameter** (optional): `upload_to`.
    - **Example**:
      ```python
      photo = models.ImageField(upload_to='photos/')
      ```
      **SQL Equivalent**: `photo VARCHAR(100)`

22. **JSONField**
    - **Purpose**: Stores JSON data (native JSON support in PostgreSQL; serialized in others).
    - **Database Data Type**: `JSON` or `JSONB` (PostgreSQL), `TEXT` (other databases).
    - **Example**:
      ```python
      metadata = models.JSONField()
      ```
      **SQL Equivalent**: `metadata JSONB` (PostgreSQL)

23. **BinaryField**
    - **Purpose**: Stores raw binary data.
    - **Database Data Type**: `BYTEA` (PostgreSQL) or `BLOB` (other databases).
    - **Example**:
      ```python
      data = models.BinaryField()
      ```
      **SQL Equivalent**: `data BYTEA` (PostgreSQL)

### **Relationship Fields**

24. **ForeignKey**
    - **Purpose**: Defines a many-to-one relationship (e.g., a book has one author).
    - **Database Data Type**: Foreign key referencing another table’s primary key (e.g., `INTEGER`).
    - **Required Parameter**:
      - `to`: The related model (e.g., `Author`).
      - `on_delete`: Behavior when the referenced object is deleted (e.g., `models.CASCADE`).
    - **Example**:
      ```python
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
      ```
      **SQL Equivalent**: `author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE`

25. **OneToOneField**
    - **Purpose**: Defines a one-to-one relationship (e.g., an author has one profile).
    - **Database Data Type**: Foreign key with a unique constraint.
    - **Required Parameter**:
      - `to`: The related model.
      - `on_delete`: Behavior when the referenced object is deleted.
    - **Example**:
      ```python
      profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
      ```
      **SQL Equivalent**: `profile_id INTEGER UNIQUE REFERENCES profiles(id) ON DELETE CASCADE`

26. **ManyToManyField**
    - **Purpose**: Defines a many-to-many relationship (e.g., a book can have multiple genres).
    - **Database Data Type**: Creates a junction table with foreign keys.
    - **Required Parameter**:
      - `to`: The related model.
    - **Example**:
      ```python
      genres = models.ManyToManyField(Genre)
      ```
      **SQL Equivalent**: Creates a table like `book_genres(book_id, genre_id)` with foreign keys.

---


- **Choosing the Right Field**:
  - Use `CharField` for short strings, `TextField` for long text.
  - Use `DecimalField` for precise numbers (e.g., currency), `FloatField` for approximate numbers.
  - Use `JSONField` for flexible, unstructured data (especially in PostgreSQL).
  - Use relationship fields (`ForeignKey`, `OneToOneField`, `ManyToManyField`) for relational data.

- **Database Portability**:
  - Most fields work consistently across databases, but some (e.g., `JSONField`, `UUIDField`) have native support only in PostgreSQL.
  - Use `migrate` to ensure schema compatibility with your database backend.

---
## **3. CRUD Operations**
Django ORM provides methods to perform Create, Read, Update, and Delete operations.

### **Create**
Insert a new record into the database.
```python
# Method 1: Using create()
author = Author.objects.create(name="J.K. Rowling", email="jk@example.com")

# Method 2: Using save()
author = Author(name="Stephen King", email="king@example.com")
author.save()
```

### **Read**
Retrieve records from the database.
```python
# Get all records
authors = Author.objects.all()

# Get single record by primary key
author = Author.objects.get(pk=1)

# Filter records
authors = Author.objects.filter(name__startswith="J")

# Get first or last record
first_author = Author.objects.first()
last_author = Author.objects.last()
```

### **Update**
Modify existing records.
```python
# Update single record
author = Author.objects.get(pk=1)
author.name = "Joanne Rowling"
author.save()

# Update multiple records
Author.objects.filter(name__startswith="J").update(email="new@example.com")
```

### **Delete**
Remove records from the database.
```python
# Delete single record
author = Author.objects.get(pk=1)
author.delete()

# Delete multiple records
Author.objects.filter(name__startswith="J").delete()
```

### **Explanation**
- **`objects`**: The default manager for models, used to query the database.
- **`create()`**: Inserts a new row and returns the object.
- **`get()`**: Retrieves a single record; raises `DoesNotExist` if not found.
- **`filter()`**: Returns a QuerySet matching the criteria.
- **`save()`**: Persists changes to the database.
- **`delete()`**: Removes the record(s) from the database.

---

## **4. QuerySet API**
A QuerySet is a lazy-evaluated collection of database queries. It allows chaining of filters, ordering, and other operations.

### **Common QuerySet Methods**
```python
# Filtering
authors = Author.objects.filter(name__icontains="rowling")  # Case-insensitive search
authors = Author.objects.exclude(name__startswith="J")  # Exclude records

# Ordering
authors = Author.objects.order_by('name')  # Ascending
authors = Author.objects.order_by('-name')  # Descending

# Slicing
authors = Author.objects.all()[:5]  # First 5 records

# Chaining
authors = Author.objects.filter(name__startswith="J").order_by('created_at')[:2]
```

### **Field Lookups**
Field lookups allow precise filtering.
```python
# Exact match
Author.objects.filter(name__exact="J.K. Rowling")

# Case-insensitive match
Author.objects.filter(name__iexact="j.k. rowling")

# Contains
Author.objects.filter(email__contains="@example.com")

# Greater than / Less than
Author.objects.filter(created_at__gt="2025-01-01")
Author.objects.filter(created_at__lte="2025-06-12")

# In a list
Author.objects.filter(name__in=["J.K. Rowling", "Stephen King"])
```

### **Explanation**
- **Lazy Evaluation**: QuerySets are not executed until evaluated (e.g., by iterating or calling `list()`).
- **Field Lookups**: Use `__` to specify conditions (e.g., `name__startswith`).
- **Chaining**: Combine multiple operations for complex queries.
- **SQL Generation**: Django translates QuerySets into optimized SQL queries.

---

## **5. Relationships**
Django ORM supports three types of relationships: **ForeignKey**, **OneToOneField**, and **ManyToManyField**.

### **ForeignKey (Many-to-One)**
A book has one author, but an author can have many books.
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Create related objects
author = Author.objects.create(name="J.K. Rowling", email="jk@example.com")
book = Book.objects.create(title="Harry Potter", author=author)

# Query related objects
books = author.book_set.all()  # Get all books by an author
author = book.author  # Get the author of a book
```

### **OneToOneField**
Each author has one profile, and each profile belongs to one author.
```python
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()

# Create related objects
profile = Profile.objects.create(author=author, bio="Fantasy writer")

# Query related objects
profile = author.profile  # Get author's profile
author = profile.author  # Get profile's author
```

### **ManyToManyField**
A book can have multiple genres, and a genre can belong to multiple books.
```python
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

# Create related objects
genre1 = Genre.objects.create(name="Fantasy")
genre2 = Genre.objects.create(name="Adventure")
book = Book.objects.create(title="Harry Potter")
book.genres.add(genre1, genre2)

# Query related objects
genres = book.genres.all()  # Get all genres of a book
books = genre1.book_set.all()  # Get all books in a genre
```

### **Explanation**
- **`ForeignKey`**: Creates a many-to-one relationship with an `author_id` column in the `books` table.
- **`on_delete`**: Specifies what happens when the referenced object is deleted (e.g., `CASCADE` deletes related objects).
- **`OneToOneField`**: Creates a one-to-one relationship with a unique foreign key.
- **`ManyToManyField`**: Creates a junction table (e.g., `book_genres`) to store relationships.
- **Reverse Relationships**: Access related objects using `_set` (e.g., `author.book_set`).

---

## **6. Aggregations and Annotations**
Django ORM supports aggregating data (e.g., count, sum) and annotating QuerySets with computed values.

### **Aggregation**
```python
from django.db.models import Count, Avg, Sum, Max, Min

# Count total authors
total_authors = Author.objects.count()

# Count books per author
authors = Author.objects.annotate(book_count=Count('book'))
for author in authors:
    print(author.name, author.book_count)

# Get latest publication date
latest_date = Book.objects.aggregate(Max('published_date'))
```

### **Annotation**
Add computed fields to QuerySets.
```python
from django.db.models import F

# Annotate authors with their email domain
authors = Author.objects.annotate(email_domain=F('email').split('@')[1])

# Annotate books with a flag if published recently
from django.db.models import ExpressionWrapper, BooleanField
from datetime import datetime, timedelta
recent_threshold = datetime.now() - timedelta(days=365)
books = Book.objects.annotate(
    is_recent=ExpressionWrapper(
        Q(published_date__gte=recent_threshold),
        output_field=BooleanField()
    )
)
```

### **Explanation**
- **Aggregation**: Uses functions like `Count`, `Sum`, `Avg`, `Max`, `Min` to compute values.
- **Annotation**: Adds temporary fields to each object in the QuerySet using `F` expressions or custom logic.
- **SQL**: Aggregations and annotations are translated into `GROUP BY` and computed columns in SQL.

---

## **7. Raw SQL Queries**
When ORM is insufficient, you can execute raw SQL queries.

### **Syntax**
```python
# Raw query returning model instances
authors = Author.objects.raw('SELECT * FROM authors WHERE name LIKE %s', ['J%'])

# Raw query returning raw data
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('SELECT name, email FROM authors')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

### **Explanation**
- **`raw()`**: Returns model instances for the query.
- **Connection**: Use `django.db.connection` for direct database access.
- **Security**: Always use parameterized queries to prevent SQL injection.

---

## **8. Database Transactions**
Django ensures database operations are atomic to maintain data integrity.

### **Syntax**
```python
from django.db import transaction

# Atomic transaction
@transaction.atomic
def create_author_and_book(name, email, book_title):
    author = Author.objects.create(name=name, email=email)
    Book.objects.create(title=book_title, author=author)

# Manual transaction
with transaction.atomic():
    author = Author.objects.create(name="J.K. Rowling", email="jk@example.com")
    Book.objects.create(title="Harry Potter", author=author)
```

### **Explanation**
- **Atomicity**: Ensures all operations succeed or none are applied.
- **`@transaction.atomic`**: Decorates functions to run in a transaction.
- **`with transaction.atomic()`**: Defines a transaction block.
- **Rollback**: If an error occurs, changes are rolled back.

---

## **9. Indexes and Constraints**
Django allows defining indexes and constraints to optimize queries and enforce rules.

### **Syntax**
```python
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),  # Single-field index
            models.Index(fields=['name', 'email'], name='name_email_idx'),  # Composite index
        ]
        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='unique_name_email'),
            models.CheckConstraint(check=models.Q(name__gt=''), name='non_empty_name'),
        ]
```

### **Explanation**
- **Indexes**: Improve query performance (e.g., for `filter(name=...)`).
- **Constraints**: Enforce rules like uniqueness or data validation.
- **SQL**: Indexes create `CREATE INDEX` statements; constraints create `UNIQUE` or `CHECK` constraints.

---

## **10. Database Configuration**
Configure the database in `settings.py`.

### **Syntax**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **Explanation**
- **ENGINE**: Specifies the database backend (e.g., `postgresql`, `mysql`, `sqlite3`).
- **NAME**: Database name or file path (for SQLite).
- **Credentials**: User, password, host, and port for connection.
- **Multiple Databases**: Define additional databases under other keys.




