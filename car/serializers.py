from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True, max_length=64)
    model = serializers.CharField(required=True, max_length=64)
    horse_powers = serializers.IntegerField()
    is_broken = serializers.BooleanField(default=False)
    problem_description = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    def validate_horse_powers(self, value):
        if value < 1 or value > 1914:
            raise serializers.ValidationError("incorrect horse power value")
        return value

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get(
            "manufacturer",
            instance.manufacturer
        )
        instance.model = validated_data.get(
            "model",
            instance.model
        )
        instance.horse_powers = validated_data.get(
            "horse_powers",
            instance.horse_powers
        )
        instance.is_broken = validated_data.get(
            "is_broken",
            instance.is_broken
        )
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.problem_description
        )
        instance.save()
        return instance
