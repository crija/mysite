from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from polls.models import People

from polls.models import Pet

def index(request):
    return HttpResponse("""<h1>Oba!!!Seu cadastro foi finalizado com sucesso!</h1>
    <p>Agora é só acompanhar o sorteio semanalmente e torcer!</p>
    INDICANDO AMIGOS VOCÊ TEM MAIS CHANCE DE SER O PRÓXIMO GANHADOR $$$
    <h1>BOA SORTE!!!</h1>
    """)

def criar(request):
    return HttpResponse("""Preencha com seus dados corretos para não ocasionar em probremas futuros!
    <hr>
<form>
  <label for="fname">Nome*</label><br>
  <input type="text" id="fname" name="fname"><br>
  <label for="lname">Sobrenome*</label><br>
  <input type="text" id="lname" name="lname"><br>
  <label for="e-mail">E-mail*</label><br>
  <input type="text" id="e-mail" name="e-mail"><br>
  <label for="senha">Criar Senha*</label><br>
  <input type="text" id="Senha se acesso" name="Senha"><br

  <p>Deseja receber nossas promoções por e-mail?</p>

  <input type="radio" id="sim" name="fav_lenguage" value="">
  <label for="sim">SIM</label><br>
  <input type="radio" id="não" name="fav_language" value="">
  <label for="não">NÃO<label><br>
  <hr>
  <input type="submit" value="Enviar Cadastro">

  <a href="http://127.0.0.1:8000/polls">Clique aqui</a>
</form>
""")

def cadastro(request):
    return HttpResponse("""Seu cadastro foi finalizado
    <a href="/polls">Ir para a pagina de polls</a>

    """)


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

def exer(request):
    return HttpResponse("""<title>Parágrafos</title>
</head>
<body>
    <hr>
    <h1>Jogo da Fortuna$$$</h1>
    <hr>
    <p>Cadastre-se e concorra a premios imperdíveis!!!</p>

    Deseja se cadastrar?

<form>
    <input type="checkbox" id="sim" name="fav_lenguage" value="">
    <label for="sim">SIM</label><br>
    <input type="checkbox" id="não" name="fav_language" value="">
    <label for="não">NÃO<label><br>

    <p>Se você respondeu 'SIM'. Clique no link a seguir:<p>

    <a href="criar">CLIQUE AQUI</a>
<form>

</body>
</html>""")

def detail(request, question_id):
    return HttpResponse("You're looking at the question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def view_people(request, people_id):
    pessoa = People.objects.filter(id=people_id)[0]
    return HttpResponse(f"O nome da pessoa de id = {people_id}, é {pessoa.nome} e a idade é {pessoa.idade}")

def view_pet(request, pet_id):
    animal = Pet.objects.filter(id = pet_id)[0]
    pessoas = People.objects.filter(id = animal.people_id)[0]
    return HttpResponse(f"O nome do pet com id = {pet_id}, é {animal.nome} é da pessoa com id = {animal.people_id}, é {pessoas.nome}")
