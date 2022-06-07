from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")