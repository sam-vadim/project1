from django.http import HttpResponse
from prog1.models import Person
from rest_framework import views, status
from rest_framework.response import Response
from prog1.serializers import PersonSerializer

class Index(views.APIView):

    def get(self, request):
        data_all = Person.objects.all()
        serializer = PersonSerializer(data_all, many=True)
        # if serializer.is_valid():
        #    return Response(data={'status': 'dsgsgfdsgfds'}, status=200)
        return HttpResponse(serializer.data)


class About(views.APIView):

    def get(self, request):

        try:
            data_one = Person.objects.get(id=5)
        except Person.DoesNotExist:
            return HttpResponse(f'<h2>Нет данных для запроса</h2>')
        except Person.MultipleObjectsReturned:
            return HttpResponse(f'<h2>Данные в запросе повторяются</h2>')

        serializer = PersonSerializer(data_one).data
        # if serializer.is_valid():
        #     s = serializer.validated_data

        return Response(serializer)


class Contact(views.APIView):

    def get(self, request):
        return HttpResponse("<h2>Контакты</h2>")
