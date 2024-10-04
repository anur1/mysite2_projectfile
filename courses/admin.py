from django.contrib import admin
from .models import Course, Category, Slider
from django_summernote.admin import SummernoteModelAdmin #summernote1
#%pip install django-summernote #summernote0
# Register your models here.




@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", 
                    "isActive", "category_list", "isHome",)
    list_display_links = ("title", "slug",)
    prepopulated_fields = {"slug": ("title",), }
    list_filter = ("title", "slug",  "isActive","isHome" )
    list_editable = ("isActive", "isHome")
    search_fields = ("title", )
    summernote_fields = ('content',)  #summernote-editor0

    def category_list(self, obj):
        html = ""
        # gelen kurs objesinin dahil olduğu bütün kategoriler = obj.categories.all()
        for category in obj.categories.all():
            html += category.name + '  '

        return html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "course_count")
    prepopulated_fields = {"slug": ("name",), }

    def course_count(self, obj):
        return obj.course_set.count()
    

#slider'ı admin panele ekleme
admin.site.register(Slider)

""