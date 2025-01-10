import graphene
from .models import Car
from graphene_django.types import DjangoObjectType

class CarType(DjangoObjectType):
    class Meta:
        model = Car

class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)

    def resolve_all_cars(root, info):
        return Car.objects.all()

class CreateCar(graphene.Mutation):
    class Arguments:
        model = graphene.String(required=True)
        license_plate = graphene.String(required=True)
        color = graphene.String(required=True)
        service_type = graphene.String(required=True)

    car = graphene.Field(CarType)

    def mutate(root, info, model, license_plate, color, service_type):
        car = Car(
            model=model,
            license_plate=license_plate,
            color=color,
            service_type=service_type,
        )
        car.save()
        return CreateCar(car=car)

class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()