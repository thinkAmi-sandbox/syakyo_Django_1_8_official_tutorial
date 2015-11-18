from django.contrib import admin

from .models import Question

# カスタマイズ無し
# admin.site.register(Question)

# 列の並び順をカスタマイズ
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)

# 列の区切りをカスタマイズ
class QuestionAdmin2(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'] }),
    ]
# admin.site.register(Question, QuestionAdmin2)

# 列の表示を隠す
class QuestionAdmin3(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
admin.site.register(Question, QuestionAdmin3)
