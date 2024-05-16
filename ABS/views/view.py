from  django.http import HttpResponse,HttpResponseNotFound
from django.db import connection
from django.shortcuts import render,redirect
from ..models import company_master,State_Master,ledger
from django.contrib import messages
from ..forms import company_master_form
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url="/admin") 
def Home(request):
    return render(request,"index.html",context={'title':"DashBoard"}) 
 
@login_required(login_url="/admin")  
def CompanyMaster(request,type="new"):
    cmdatas=company_master.objects.raw('SELECT am.id,am.companyname,am.mailid,am.district,am.phone,am.gst,ast.state FROM absys_django.abs_company_master am,absys_django.abs_state_master ast where am.state=ast.code')  
    state_data=State_Master.objects.all()
    if(type=='Data'):
         return render(request,"./Masters/company/Table.html",context={
         'title':"company Master",'data':cmdatas,'state':state_data
           },content_type="text/html",status=200) 
    elif(type=='new'):
          return render(request,"./Masters/company/company.html",context={
         'title':"Data",'state':state_data
           },content_type="text/html",status=200) 
        
    

def Unitmaster(request):
    cmdatas=company_master.objects.all(); 
    state_data=State_Master.objects.all()
    return render(request,"./Masters/unit/unitlist.html",context={
         'title':"company Master",'data':cmdatas,'state':state_data
           }) 
        
     
def TableModification(request,redir,modelTable):
   if request.method=="POST":
           dumps=json.dumps(request.POST)
           data=json.loads(dumps)
           dis=dict(data)
           dis.pop("csrfmiddlewaretoken")
           cmpsave=""
           if(modelTable=="cm"):
             cmpsave=company_master(**dis)
           elif(modelTable=="led"):
              cmpsave=ledger(**dis)
           cmpsave.save()
           messages.success(request, "Save successfully.")
           return redirect(redir,type="new")
              
   elif(request.method=="DELETE"):
         data=json.loads(request.body)
         cmdelete=""
         if(modelTable=="cm"):
            cmdelete=company_master.objects.filter(id=data["id"]).delete()
        
         elif(modelTable=="led"):
            cmdelete=ledger.objects.filter(id=data["id"]).delete()
            
         return HttpResponse(cmdelete)
   elif(request.method=="PUT"):
         data=json.loads(request.body)
         disdata={""+data['feild']:""+data["value"]}
         if(modelTable=="cm"):
           company_master.objects.filter(id=data["id"]).update(**disdata)
           
         elif(modelTable=="led"):
            ledger.objects.filter(id=data["id"]).update(**disdata)
           
         return HttpResponse(data)
       
     
  
def page404(request,exception):
    return render(request,"error404.html",context={"err":exception})


def Ledger(request,type="new"):
    cmdatas=company_master.objects.raw("SELECT am.id,am.address,am.ledgername,am.mailid,am.district,am.gst,ast.state FROM absys_django.abs_ledger am,absys_django.abs_state_master ast where am.state=ast.code and am.active='y'")
    state_data=State_Master.objects.all()
    if(type=='Data'):
         return render(request,"./Masters/ledger/Table.html",context={
         'title':"company Master",'data':cmdatas,'state':state_data
           },content_type="text/html",status=200) 
    elif(type=='new'):
          return render(request,"./Masters/ledger/ledger.html",context={
         'title':"Data",'state':state_data
           },content_type="text/html",status=200) 
          
          
          
        