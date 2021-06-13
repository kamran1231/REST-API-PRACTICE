
from rest_framework import serializers
from watchlist_app.models import Movie


'''<=====>Validators<=====>'''
def name_length(value):
    if len(value) > 10:
        raise serializers.ValidationError('Name should not be greater than 10 character')
    return value


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()


    def create(self,validated_data):
        return Movie.objects.create(**validated_data)


    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)

        instance.save()
        return instance

    '''<=====>Object-level Validation<=====>'''
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description should not be same")
        return data



    '''<=====>Field-level Validation<=====>'''
    def validate_name(self,value):
        if len(value) <= 3:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value

    

