from django.contrib import admin

from .models import Choice, Question

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
# admin.site.register(Question, QuestionAdmin3)


# Choice model の画面への追加
# admin.site.register(Choice)

# QuestionとChoiceの登録を一括で行う
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# table-baseなフォーマットの場合
class ChoiceInline2(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin4(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inlines = [ChoiceInline] #標準的な一括登録
    inlines = [ChoiceInline2]   # テーブル的な表現のコンパクトな一括登録

    # 一覧画面で表示する項目
    # modelの関数も表示できる
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 一覧画面でフィルターできる項目、右側にフィルタ情報が出てくる
    list_filter = ['pub_date']

    # 一覧画面で検索できる項目、ヘッダの上に検索項目が出てくる
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin4)