from django.contrib import admin
from reviews.models import Category, Comment, CustomUser, Genre, Review, Title


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email',
                    'first_name', 'last_name', 'role',
                    'confirmation_code', 'password')
    list_editable = ('role', )
    search_fields = ('username',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")


class GenreAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")


class GenreTitleAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "year", "description", "category")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "title", "author", "score", "pub_date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "review", "author", "pub_date")


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, GenreTitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
