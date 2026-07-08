from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ExpenseViewSet(ModelViewSet):
    queryset=Expense.objects.all()
    serializer_class=ExpenseSerializer