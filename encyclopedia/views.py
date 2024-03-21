from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random

def convert(title):
    contenido = util.get_entry(title)
    markdowner = Markdown()
    if contenido is None:
        return None
    else:
        return markdowner.convert(contenido)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def entryPage(request, title):
    HTMLconverted = convert(title)
    if HTMLconverted is None:
        return render(request, "encyclopedia/error.html")
    
    else:
        return render(request, "encyclopedia/entryPage.html",{
            "title" : title,
            "contenido" : HTMLconverted  
        })
        
def search(request):
    if request.method == "POST":
        busqueda = request.POST.get('q') 
        HTMLconverted = convert(busqueda)
        if HTMLconverted is not None:
            return render(request, "encyclopedia/entryPage.html", {
                "title": busqueda,
                "contenido": HTMLconverted  
            }) 
        else: 
            entries = util.list_entries()
            recomendacion = [entry for entry in entries if busqueda.lower() in entry.lower()]
            return render(request, "encyclopedia/search.html", {
                "recomendacion": recomendacion
            })
    else:
        return render(request, "encyclopedia/error.html")
    
def randomm(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    HTMLconverted = convert(random_entry)
    return render(request, "encyclopedia/entryPage.html", {
        "title": random_entry,
        "contenido": HTMLconverted
    })    
    

def edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    else:
        return render(request, "error.html", {
            "msg": "Only POST method is allowed for editing."
        })
        
def save(request):
    if request.method == 'POST':
        title = request.POST['title']
        contenido = request.POST['contenido']
        util.save_entry(title,contenido)
        contenido = convert(title)
        return render (request,"encyclopedia/entryPage.html",{
            "title": title,
            "contenido": contenido
            })
        
def newPage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newPage.html")
    else:
        title = request.POST['title']
        contenido = request.POST ['contenido']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render (request, "encyclopedia/error.html", {
            "msg": "Entry page already exists"
            })
        else:
            util.save_entry(title,contenido )
            contenido = convert(title)
            return render (request,"encyclopedia/entryPage.html",{
            "title": title,
            "contenido": contenido
            })