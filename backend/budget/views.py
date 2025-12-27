from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def calculate_budget(request):
    amount = request.GET.get("amount")
    if not amount:
        return JsonResponse({"status": "Error", "message": "No amount provided."})

    amount = float(amount)

    # super simple logic for demo
    if amount <= 1000:
        status = "Certified Flex"
        message = "You can afford this!"
    else:
        status = "Financial Crime"
        message = "Better save first."

    return JsonResponse({"status": status, "message": message})