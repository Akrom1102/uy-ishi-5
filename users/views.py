from django.shortcuts import render


def user_list(request):
    return render(request, 'users_page.html')


def user_detail_page(request):
    return render(request, 'user_details.html')