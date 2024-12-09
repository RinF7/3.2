from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Publishers"

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='book_list', default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['publication_date']
        unique_together = ['publication_date', 'category']

    def __str__(self):
        return self.title