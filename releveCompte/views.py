from django.shortcuts import render
from .models import  ReleveCompte,Image
from django.http import HttpResponse
from .forms import ReleveCompteForm
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import  FileResponse
import io 
from io import BytesIO
from django.contrib import messages
from tablib import Dataset
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views import View
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.decorators import login_required
#from reste_framework.authtoken.models import Token

# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch 
# from reportlab.lib.pagesizes import letter

# -*- coding: cp1252 -*-

"""
Traduction d'un nombre en texte.
Réalisation : Michel Claveau    http://mclaveau.com

SVP, n'enlevez pas mon adresse/URL ; merci d'avance

Usage : voir les exemples, à la fin du script.

Note : traduction franco-française, avec unités variables, orthographe géré, unités et centièmes.
"""
num=0
def save_pdf(params:dict):
    template = get_template("template.html")
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')),response)
    file_name = uuid.uuid4()
    try:  
        with open(str(settings.BASE_DIR) + f'/public/static/{file_name}.pdf', 'wb+') as output: 
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')),output)

        
    except Exception as e:
        print(e)
        print("probleme d'afficharge")

    

    if  pdf.err:
        return '' , False
    return file_name, True


class ViewPDF(View):
    def get(self, request,*args,**kwargs):
        pdf = render_to_pdf(template.html)
        return HttpResponse(pdf,content_type='application/pdf')
# def pdf(request):
#     buf= io.BytesIO()
#     c= canvas.Canvas(buf,pagesize=letter,bottomup=0)
#     #create the text object
#     textob = c.beginText()
#     textob.setTextOrigin(inch,inch)
#     textob.setFont("Helvetica",14)

class GeneratePdf(APIView):
    def get(self, request):
        releve = ReleveCompte.objects.get(numero=9134)
        params={

            'releve':releve
            
        }
        file_name, status = save_pdf(params)
        if not status:
            return HttpResponse({'test impression ': 400 })
        #pdf = render_to_pdf(template.html)
        return HttpResponse({'status':200,'path':f'/static/{file_name}.pdf'})
    
liste=[]
def simple_upload(request):
    
    if request.method == 'POST':
        #person_resource = PersonneResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)
        montant=0
        i=0
        num=0
        for data in imported_data:
            for elt in data:
                i=i+1
                if i==49:
                    liste.append(elt)
                if i==91:
                    liste.append(elt)
                if i==99:
                     liste.append(elt)

                montant = elt
        liste.append(montant)
                

        value=ReleveCompte( 
        numero= liste[2],
        nomDestinataire  = liste[0],
        montant = liste[3])
        value.save()
    # print(liste[0])
    # print(liste[1])
    # print(liste[2])
    # print(liste[3])
    # print('***********************')
    return render(request,'input.html')
    
def tradd(num):
    global t1,t2
    ch=''
    if num==0 :
        ch=''
    elif num<20:
        ch=t1[num]
    elif num>=20:
        if (num>=70 and num<=79)or(num>=90):
            z=int(num/10)-1
        else:
            z=int(num/10)
        ch=t2[z]
        num=num-z*10
        if (num==1 or num==11) and z<8:
            ch=ch+' et'
        if num>0:
            ch=ch+' '+tradd(num)
        else:
            ch=ch+tradd(num)
    return ch


def tradn(num):
    global t1,t2
    ch=''
    flagcent=False
    if num>=1000000000:
        z=int(num/1000000000)
        ch=ch+tradn(z)+' milliard'
        if z>1:
            ch=ch+'s'
        num=num-z*1000000000
    if num>=1000000:
        z=int(num/1000000)
        ch=ch+tradn(z)+' million'
        if z>1:
            ch=ch+'s'
        num=num-z*1000000
    if num>=1000:
        if num>=100000:
            z=int(num/100000)
            if z>1:
                ch=ch+' '+tradd(z)
            ch=ch+' cent'
            flagcent=True
            num=num-z*100000
            if int(num/1000)==0 and z>1:
                ch=ch+'s'
        if num>=1000:
            z=int(num/1000)
            if (z==1 and flagcent) or z>1:
                ch=ch+' '+tradd(z)
            num=num-z*1000
        ch=ch+' mille'
    if num>=100:
        z=int(num/100)
        if z>1:
            ch=ch+' '+tradd(z)
        ch=ch+" cent"
        num=num-z*100
        if num==0 and z>1:
           ch=ch+'s'
    if num>0:
        ch=ch+" "+tradd(num)
    return ch


def trad(nb, unite=" ", decim="centime"):
    global t1,t2
    nb=round(nb,2)
    t1=["","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf"]
    t2=["","dix","vingt","trente","quarante","cinquante","soixante","septante","quatre-vingt","nonante"]
    z1=int(nb)
    z3=(nb-z1)*100
    z2=int(round(z3,0))
    if z1==0:
        ch="zéro"
    else:
        ch=tradn(abs(z1))
    if z1>1 or z1<-1:
        if unite!='':
            ch=ch+" "+unite+'s'
    else:
        ch=ch+" "+unite
    if z2>0:
        ch=ch+tradn(z2)
        if z2>1 or z2<-1:
            if decim!='':
                ch=ch+" "+decim+'s'
        else:
            ch=ch+" "+decim
    if nb<0:
        ch="moins "+ch
    return ch


def tableau(request):
    return render(request, 'tableau.html')





def template(request):
    return render(request, 'template.html')


def ajoutMontant (request):
    data=dict()
    
    if request.method=='POST':
        num = request.POST.get('numero')
        dest1 = request.POST.get('sign1')
        dest2 = request.POST.get('sign2')
        releve = ReleveCompte.objects.get(numero=num)
        releve.signataire2=dest1
        releve.signataire3=dest2
        releve.save(update_fields=['signataire2','signataire3'])

        
        print(datetime.now())
        nombrelettre=trad(releve.montant)
    
    return render(request,'template.html',{'releve':releve,'dest1':dest1,'dest2':dest2,'nombrelettre':nombrelettre})

    
    # if request.method == 'POST':
    #     if form.is_valid():
    #         montant = request.POST.get('montant')
    #         numero = request.POST.get('numero') 
    #         releve =  ReleveCompte.objects.filter('numero')
    #         print(request.POST)


def ajoutMontante (request):
    data=dict()
    
    if request.method=='POST':
        num = request.POST.get('numero')
        dest1 = request.POST.get('sign1')
        dest2 = request.POST.get('sign2')
        releve = ReleveCompte.objects.get(numero=num)
        releve.signataire2=dest1
        releve.signataire3=dest2
        releve.save(update_fields=['signataire2','signataire3'])

        
        print(datetime.now())
        nombrelettre=trad(releve.montant)
        params={
            'releve':releve,
            'dest1':dest1,
            'dest2':dest2,
            'nombrelettre':nombrelettre
        }

    file_name, status = save_pdf(params)
    if not status:
         return Response({'status': 400 })
        #pdf = render_to_pdf(template.html)
    Response({'status':200,'path':f'/media/{file_name}.pdf'})
    
    return render(request,'template.html',{'releve':releve,'dest1':dest1,'dest2':dest2,'nombrelettre':nombrelettre})

           
def imprimer(request):


    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    #p.drawString(100,100,template)
    p.drawString( 'template.html')
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def pdf_report_create(request):
    if request.method=='POST':
        num = request.POST.get('numero')
        dest1 = request.POST.get('sign1')
        dest2 = request.POST.get('sign2')
        print(num)
        releve = ReleveCompte.objects.get(numero=num)
        releve.signataire2=dest1
        releve.signataire3=dest2
        releve.save(update_fields=['signataire2','signataire3'])
        nombrelettre=trad(releve.montant)
    
    
        # today = datetime.now()

        # print(datetime.now())
      

    template_path = 'template.html'
    image = Image.objects.all()
    context = {
         'releve':releve,
         'dest1':dest1,
         'dest2':dest2,
         'nombrelettre':nombrelettre,
         'image':image

         }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] =  'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    image = Image.objects.all()
     
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    #return render(request,'template.html', context)

    return response

def registerPage(request):
    context = {}
    return render(request,'account/register.html')

def loginPage(request):
    context ={}
    return render(request,'account/login.html')

def vuechef(request):
    return render(request,'indexchef.html')

def vuesecretaire(request):
    return render(request,'indexsecretaire.html')