from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProdViews(APIView):
    def get(self,request):
        viewallprods=Products.objects.all()
        
        serializedproduct=AllproductDtls_Serializers(viewallprods,many=True).data
        
        return Response(serializedproduct)

    def post(self,request):        
        newprods=AllproductDtls_Serializers(data=request.data)
        if newprods.is_valid():
            newprods.save()
            return Response("Data saved")
        else:
            return Response(newprods.errors)
    

class ProdViewsbyID(APIView):
    def get(self,request,id):
        items=Products.objects.get(id=id)
        singleItembyid=SingleProdDtls_Serializers(items).data   
        return Response(singleItembyid)
    
    def patch(self,request,id):
        UpdateProd=Products.objects.filter(id=id)

        UpdateProd.update(pname=request.data['pname'],
                          pcode=request.data['pcode'],
                          pprice=request.data['pprice'],
                          categoryid_id=request.data['categoryid'])
        
        return Response("Updated")
    
    def delete(self,request,id):

        DeleteProd=Products.objects.get(id=id)

        DeleteProd.delete()

        return Response("Producted Deleted")
        

class categoryview(APIView):
    def get(self,request):        
        allcategory=category_Serializers(Category.objects.all(),many=True).data
        return Response(allcategory)
    
    def post(self,request):        
        newcat=category_Serializers(data=request.data)
        if newcat.is_valid():
            newcat.save()
            return Response("Data saved")
        else:
            return Response(newcat.errors)

class catViewsByID(APIView):
    def get(self,request,id):
        Catitems=Category.objects.get(id=id)
        CatItembyid=category_Serializers(Catitems).data   
        return Response(CatItembyid)
    
    def patch(self,request,id):
        UpdateCat=Category.objects.filter(id=id)
        UpdateCat.update(categoryname=request.data['categoryname'])
        return Response("Updated")
    
    def delete(self,request,id):

        DeleteCat=Category.objects.get(id=id)

        DeleteCat.delete()

        return Response("Category Deleted")