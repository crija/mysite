from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def criar(request):
    return HttpResponse("""<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname"><br>
  <input type="submit" value="criar">
</form>
""")

def cadastro(request):
    return HttpResponse("Seu cadastro foi finalizado")

def recursos(request):
    return HttpResponse("""<p>Qual dado você deseja enviar?</p>

<form>
  <input type="checkbox" id="nome" name="fav_language" value="">
  <label for="nome">NOME</label><br>
  <input type="checkbox" id="idade" name="fav_language" value="">
  <label for="idade">IDADE</label><br>
  <input type="checkbox" id="email" name="fav_language" placeholder="">
  <label for="email">EMAIL</label>
</form>""")
