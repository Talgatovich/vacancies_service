from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from vacancies.models import Vacancy
from .serializers import VacancySerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class VacancyAPIView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'index.html'
	serializer_class = VacancySerializer

	def get(self, request):
		queryset = Vacancy.objects.all()
		serializer = VacancySerializer(queryset, many=True).data
		return Response({'vacancies': serializer})


class VacancyDetail(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'vacancy_detail.html'
	serializer_class = VacancySerializer

	def get(self, request, pk):
		vacancy = Vacancy.objects.all().get(pk=pk)
		serializer = VacancySerializer(vacancy).data
		return Response({'vacancy': serializer})
#
# class ProfileList(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_list.html'
#
#     def get(self, request):
#         queryset = Profile.objects.all()
#         return Response({'profiles': queryset})
#
#
