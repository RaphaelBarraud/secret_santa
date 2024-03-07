from rest_framework import serializers
from .models import Draw, DrawResult


class DrawResultSerializer(serializers.ModelSerializer):
    """ Serializer used for the DrawResult """
    class Meta:
        model = DrawResult
        fields = ['id', 'draw', 'giver', 'receiver']
        read_only_fields = ('draw',)


class DrawSerializer(serializers.ModelSerializer):
    """ Serializer used for the draw except for the create method """
    # Connect to the DrawResult serializer
    draw_result = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Draw
        fields = ['id', 'name', 'creation_time', 'draw_result']
        read_only_fields = ('creation_time',)


class DrawPostSerializer(serializers.ModelSerializer):
    """ Serializer used for the draw create method """
    # Connect to the DrawResult serializer
    draw_result = DrawResultSerializer(many=True)
    class Meta:
        model = Draw
        fields = ['id', 'name', 'creation_time', 'draw_result']
        read_only_fields = ('creation_time',)

    def create(self, validated_data):
        """ 
        Method to copy the nested serializers

        Args:
            validated_data(dict): data to copy in the DB

        Returns:
            draw(Draw): return our draw object
        """
        draw_result = validated_data.pop('draw_result')
        draw = Draw.objects.create(**validated_data)
        for result in draw_result:
            DrawResult.objects.create(draw_id=draw.id, **result)
        return draw