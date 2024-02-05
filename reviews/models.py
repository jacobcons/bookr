from django.db import models
from django.contrib import auth


# Create your models here.
class Publisher(models.Model):
    """A company that publishes books"""

    name = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Contributor(models.Model):
    """A contributor to a book"""

    first_names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_names


class Book(models.Model):
    """A published book"""

    title = models.CharField(max_length=70)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, through="BookContributor")

    def __str__(self):
        return self.title


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(
        null=True, help_text="The last date and time the review was edited"
    )
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
