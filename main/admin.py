from django.contrib import admin
from .models import  *

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
    search_fields = ('title', ) 


@admin.register(AddictionQuestion)
class AddictionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'yes', 'no', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(AnxietyQuestion)
class AnxietyAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(D_A_S_SQuestion)
class D_A_S_SAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately' , 'most_of_the_time', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(DepressionQuestion)
class DepressionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(HostilityQuestion)
class HostilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')


@admin.register(InsomniaQuestion)
class InsomiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'true', 'false', 'test_id']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(InterpersonalSensitivityQuestion)
class InterpersonalSensitivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(NeuroticismQuestion)
class NeuroticismAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(O_C_DQuestion)
class O_C_DAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(ParanoiaQuestion)
class ParanoiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(ParentsPediatricSymptomQuestion)
class ParentsPediatricSymptomAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'never', 'sometimes', 'often', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(PersonalHealthQuestion)
class PersonalHealthAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(PersonalityQuestion)
class PersonalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'disagree_strongly', 'disagree_a_little', 'neither_agree_nor_disagree', 'agree_a_little', 'agree_strongly', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(PhobiaQuestion)
class PhobiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(PsychoticismQuestion)
class PsychoticismAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

    
@admin.register(SleepApneaQuestion)
class SleepApneaAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'true', 'false', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(SomatizationQuestion)
class SomatizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'not_at_all', 'a_little_bit', 'moderately', 'quite_a_bit', 'extremely', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(StressTestQuestion)
class StressTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'yes', 'no', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')

@admin.register(YouthsPediatricSymptomQuestion)
class YouthsPediatricSymptomAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'never', 'sometimes', 'often', 'date_created']
    search_fields = ('question', )
    ordering = ('id', 'date_created')


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['test', 'fullname', 'company', 'date_taken']
    ordering = ('date_taken', )
