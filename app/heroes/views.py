from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

#from tutorials.models import Tutorial
from heroes.models import Hero
#from tutorials.serializers import TutorialSerializer
from heroes.serializers import HeroSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


""" def index(request):
    print("------------------------- I AM HERE")
    queryset = Tutorial.objects.all()
    return render(request, "tutorials/index.html", {'tutorials': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/index.html'

    def get(self, request):
        queryset = Tutorial.objects.all()
        return Response({'tutorials': queryset})


class list_all_tutorials(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tutorials/tutorial_list.html'

    def get(self, request):
        queryset = Tutorial.objects.all()
        return Response({'tutorials': queryset}) """


def index(request):
    print("------------------------- I AM HERE")
    queryset = Hero.objects.all()
    return render(request, "heroes/index.html", {'heroes': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'heroes/index.html'

    def get(self, request):
        queryset = Hero.objects.all()
        return Response({'heroes': queryset})


class list_all_heroes(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'heroes/hero_list.html'

    def get(self, request):
        queryset = Hero.objects.all()
        return Response({'heroes': queryset})

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def hero_list(request):
    if request.method == 'GET':
        heroes = Hero.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            heroes = heroes.filter(name__icontains=name)

        heroes_serializer = HeroSerializer(heroes, many=True)
        return JsonResponse(heroes_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        hero_data = JSONParser().parse(request)
        hero_serializer = HeroSerializer(data=hero_data)
        if hero_serializer.is_valid():
            hero_serializer.save()
            return JsonResponse(hero_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(hero_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Hero.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Heroes were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def hero_detail(request, pk):
    try:
        hero = Hero.objects.get(pk=pk)
    except Hero.DoesNotExist:
        return JsonResponse({'message': 'The hero does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        hero_serializer = HeroSerializer(hero)
        return JsonResponse(hero_serializer.data)

    elif request.method == 'PUT':
        hero_data = JSONParser().parse(request)
        hero_serializer = HeroSerializer(hero, data=hero_data)
        if hero_serializer.is_valid():
            hero_serializer.save()
            return JsonResponse(hero_serializer.data)
        return JsonResponse(hero_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hero.delete()
        return JsonResponse({'message': 'Hero was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)

""" @api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Tutorials were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT) """


""" @api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = TutorialSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT) """


""" @api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False) """