from django.contrib import admin

# Register your models here.
from .forms import LectureAdminForm
from .models import Course, Lecture, MyCourses

admin.site.register(MyCourses)

class LectureInline(admin.TabularInline):
    model = Lecture
    form = LectureAdminForm
    prepopulated_fields = {"slug": ("title",)}
    # raw_id_filds = 'video'
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInline]
    list_filter = ['updated', 'timestamp']
    list_display = ['title', 'updated', 'timestamp']
    readonly_fields = ['updated', 'timestamp', 'short_title']
    search_field = ['title', 'description']
    list_editable = []

    class Meta:
        model = Course

    def short_title(self, obj):
        return obj.title[:3]

admin.site.register(Course, CourseAdmin)

