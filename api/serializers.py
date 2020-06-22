from rest_framework import serializers
from main.models import *

class AddictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddictionQuestion
        fields = '__all__'

class AnxietySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnxietyQuestion
        fields = '__all__'

class D_A_S_SSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_A_S_SQuestion
        fields = '__all__'

class DepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepressionQuestion
        fields = '__all__'

class HostilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HostilityQuestion
        fields = '__all__'

class InsomniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsomniaQuestion
        fields = '__all__'

class InterpersonalSensitivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterpersonalSensitivityQuestion
        fields = '__all__'

class NeuroticismSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuroticismQuestion
        fields = '__all__'
    
class O_C_DSerializer(serializers.ModelSerializer):
    class Meta:
        model = O_C_DQuestion
        fields = '__all__'

class ParanoiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParanoiaQuestion
        fields = '__all__'

class ParentsPediatricSymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsPediatricSymptomQuestion
        fields = '__all__'

class PersonalHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalHealthQuestion
        fields = '__all__'

class PersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityQuestion
        fields = '__all__'

class PhobiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhobiaQuestion
        fields = '__all__'

class PsychoticismSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychoticismQuestion
        fields = '__all__'

class SleepApneaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepApneaQuestion
        fields = '__all__'

class SomatizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomatizationQuestion
        fields = '__all__'

class StressTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StressTestQuestion
        fields = '__all__'

class YouthsPediatricSymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouthsPediatricSymptomQuestion
        fields = '__all__'