from django.http import HttpResponse

def hello(request):
   text = """<h1>Hello Gordon!!!</h1>"""
   return HttpResponse(text)