import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(
        serializer.data,
        separators=(",", ":")
    ).encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode("utf-8")
    car_data = json.loads(json_str)
    serializer = CarSerializer(data=car_data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
