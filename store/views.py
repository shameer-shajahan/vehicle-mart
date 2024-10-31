from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from store.forms import VehicleForm,VehicleUpdateForm

from store.models import Vehicle

from django.db.models import Q

# Create your views here.

class VehicleCreateView(View):

    template_name="vehicle_add.html"

    class_name=VehicleForm

    def get(self,request,*args,**kwargs):

        form_instance=self.class_name()

        return render (request,self.template_name,{"forms":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.class_name(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)

            Vehicle.objects.create(**data) # ** to unpack the dictionary value

            return redirect("vehicle_list")

        return render (request,self.template_name,{"forms":form_instance})

class VehicleListView(View):

    template_name=("vehicle_list.html")

    def get(self,request,*arg,**kwargs):

        search_text=request.GET.get("filter")

        print(search_text)

        qs=Vehicle.objects.all()

        all_names=Vehicle.objects.values_list("name",flat=True).distinct()
   
        all_brand=Vehicle.objects.values_list("brand",flat=True).distinct()
   
        all_varient=Vehicle.objects.values_list("varient",flat=True).distinct()
   
        all_fuel_type=Vehicle.objects.values_list("fuel_type",flat=True).distinct()
   
        all_color=Vehicle.objects.values_list("color",flat=True).distinct()
   
        all_owner_type=Vehicle.objects.values_list("owner_type",flat=True).distinct()

        all_records=[]

        all_records.extend(all_names)

        all_records.extend(all_owner_type)
        
        all_records.extend(all_color)
        
        all_records.extend(all_fuel_type)
        
        all_records.extend(all_varient)
        
        all_records.extend(all_brand)

        if search_text:

            qs=qs.filter(

                Q(brand__contains=search_text)|Q(name__contains=search_text)|Q(fuel_type__contains=search_text)|Q(owner_type__contains=search_text)
                
                )

        return render(request,self.template_name,{"data":qs,"records":all_records})
    
class VehicleDetailView(View):

    template_name="Vehile_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Vehicle.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})

class VehicleDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Vehicle.objects.get(id=id).delete()

        return redirect("vehicle_list")

# class VehicleUpdateView(View):

#     template_name="vehicle_update.html"

#     class_name=VehicleForm

#     def get(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         Vehicle_objects=Vehicle.objects.get(id=id)

#         data={

#                "name":Vehicle_objects.name,

#                 "varient":Vehicle_objects.varient,

#                 "description":Vehicle_objects.description,

#                 "fuel_type":Vehicle_objects.fuel_type,

#                 "running_km":Vehicle_objects.running_km,

#                 "color":Vehicle_objects.color,

#                 "price":Vehicle_objects.price,

#                 "brand":Vehicle_objects.brand,

#                 "owner_type":Vehicle_objects.owner_type

#         }

#         form_instance=self.class_name(initial=data)

#         return render(request,self.template_name,{"forms":form_instance})
    
    
#     def post(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         form_data=request.POST

#         form_instance=self.class_name(form_data,files=request.FILES)

#         if form_instance.is_valid():

#             data=form_instance.cleaned_data
            
#             Vehicle.objects.filter(id=id).update(**data)

#             return redirect("vehicle_list")
        
#         return render(request,self.template_name,{"forms":form_instance})
    
class VehicleUpdateView(View):

    template_name="vehicle_update.html"

    form_class=VehicleUpdateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        vehicle_object=get_object_or_404(Vehicle,id=id)

        form_instance=self.form_class(instance=vehicle_object)

        return render (request,self.template_name,{"forms":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        vehicle_object=get_object_or_404(Vehicle,id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=vehicle_object)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("vehicle_list")
        
        return render(request,self.template_name,{"forms":form_instance})

            


        