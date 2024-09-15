from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from .models import Url
from .serializers import UrlSerializer

@api_view(['POST'])
def shorten_url(request):
    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        url = serializer.save()
        #.build_absolute_uri é utilizada para gerar o link de redirecionamento ja utilizando o dominio da aplicação
        short_url = request.build_absolute_uri(f"/{url.chave}/") 
        return Response({"short_url": short_url}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def redirect_url(request, chave):
    #get_object_or_404 busca o objeto da chave informada e caso não seja encontrado, retorna um erro 404
    url_instance = get_object_or_404(Url, chave=chave)
    return redirect(url_instance.url_original)
