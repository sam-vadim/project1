from django.http import HttpResponse
from prog1.models import Person
from rest_framework import views, status
from rest_framework.response import Response
from prog1.serializers import PersonSerializer, Person1Serializer

from django.utils.translation import get_language_from_request
from django.utils.translation import gettext as _

class Index(views.APIView):

    def get(self, request):
        data_all = Person.objects.all()
        serializer = PersonSerializer(data=data_all, many=True)
        if serializer.is_valid():
            return Response(data={'status': 'Data is not valid'}, status=200)

        return Response(data=serializer.data)


class About(views.APIView):

    def get(self, request):

        try:
            data_one = Person.objects.get(id=5)
        except Person.DoesNotExist:
            return HttpResponse(f'<h2>Нет данных для запроса</h2>')
        except Person.MultipleObjectsReturned:
            return HttpResponse(f'<h2>Данные в запросе повторяются</h2>')

        serializer = PersonSerializer(data_one)
        # if serializer.is_valid():
        #     s = serializer.validated_data

        str = _('Привет как дела')
        str1 = _('Дела не очень')

        return Response(serializer.data)


class PersonV(views.APIView):

    def get(self, request):

        name_id = request.GET.get('name_id')
        tom = Person.objects.filter(id=1)
        name = tom.name

        # x = request.GET.get("name")
        # y = request.GET.get("surname")
        # z = request.GET.get("age")

        return Response(data={'status': name}, status=200)

    def post(self, request):

        # tom = Person.objects.create(name="Tom", surname="Tomas", age=23)

        # return Response(tom.id)

        x = request.data.get("name")
        y = request.data.get("surname")
        z = request.data.get("age")

        Serializer1 = Person1Serializer(data=request.data)

        # if Serializer1.is_valid():
        #     sss = 'ValidAll'

        # return Response(data={'status': 'Ару ару ару'}, status=200)

        return Response(data=Serializer1.data, status=200)


# class Contact(views.APIView):
#
#     def get(self, request):
#         return HttpResponse("<h2>Контакты</h2>")
