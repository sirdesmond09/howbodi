from django.db import models
from account.models import Member

class Test(models.Model):
    title = models.CharField(max_length = 150)
    image = models.URLField(blank  = True)
    
    def __str__(self):
        return self.title
        
class InsomniaQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    true         = models.IntegerField()
    false        = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class SleepApneaQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    true         = models.IntegerField()
    false        = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)


    def __str__(self):
        return self.question

class StressTestQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    yes          = models.IntegerField()
    no           = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question
        
class PersonalHealthQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class AddictionQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    yes          = models.IntegerField()
    no           = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class SomatizationQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question


class O_C_DQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class InterpersonalSensitivityQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class DepressionQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class AnxietyQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class HostilityQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class PhobiaQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question
    
class ParanoiaQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question

class PsychoticismQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question 

class NeuroticismQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    not_at_all   = models.IntegerField()
    a_little_bit = models.IntegerField()
    moderately	 = models.IntegerField()
    quite_a_bit  = models.IntegerField()
    extremely    = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question 

class D_A_S_SQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question          = models.CharField(max_length = 500)
    not_at_all        = models.IntegerField()
    a_little_bit      = models.IntegerField()
    moderately	      = models.IntegerField()
    most_of_the_time  = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question 

class PersonalityQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question                   = models.CharField(max_length = 500)
    disagree_strongly          = models.IntegerField()
    disagree_a_little          = models.IntegerField()
    neither_agree_nor_disagree = models.IntegerField()
    agree_a_little             = models.IntegerField()
    agree_strongly             = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question 

class YouthsPediatricSymptomQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    never        = models.IntegerField()
    sometimes    = models.IntegerField()
    often        = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question 

class ParentsPediatricSymptomQuestion(models.Model):
    test         = models.ForeignKey(Test, on_delete = models.CASCADE)
    question     = models.CharField(max_length = 500)
    never        = models.IntegerField()
    sometimes    = models.IntegerField()
    often        = models.IntegerField()
    date_created = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.question 


class Assessment(models.Model):
    test       = models.ForeignKey(Test, on_delete=models.CASCADE, serialize = True)
    user       = models.ForeignKey(Member, on_delete = models.CASCADE, serialize = True)
    testname   = models.CharField(max_length = 250)
    fullname   = models.CharField(max_length = 250)
    company    = models.CharField(max_length=250)
    date_taken = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname