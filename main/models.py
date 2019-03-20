from django.db import models

# Create your models here 

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # gives the proper plural name for admin
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    # we need to know what to do with the referenced objects when the main one is deleted. 
    # When we delete a category, we don't really want to delete the tutorials from that category, 
    # nor visa versa, so instead we're opting to SET_DEFAULT here. 
    # If the category gets deleted, then the tutorials that have that category will have their categories
    # set to their default values rather than deleted.
    tutorial_category = models.ForeignKey(TutorialCategory, 
                                            default=1, 
                                            verbose_name="Category", 
                                            on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published')
    tutorial_series = models.ForeignKey(TutorialSeries, 
                                            default=1, 
                                            verbose_name="Series", 
                                            on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title