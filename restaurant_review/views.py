from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

from restaurant_review.models import Profile, Restaurant, Review

# Create your views here.

def index(request):
    print('Request for index page received')
    if request.user.is_authenticated: 
        profile = Profile.objects.get(user=request.user)
        # profile.experiment_two_day = 0
        # profile.experiment_two_last_photo_date = date(1999,1,1)
        # profile.save()

        # profile.survey_two_isComplete = False
        # profile.save()
        return render(request, 'restaurant_review/index.html', {'profile': profile})
    else: 
        return redirect('/account/login/')

def results(request):
    # User = get_user_model()
    # users = User.objects.all()
    profiles = Profile.objects.all().order_by('user__date_joined')
    # print(User.objects.values())
    return render(request, 'restaurant_review/results.html', {'all_profiles': profiles})

    # return render(request, 'restaurant_review/results.html', {'all_users': users, 'all_profiles': profiles})

def consent(request):
    profile = Profile.objects.get(user=request.user)
    profile.hasConsent = True
    profile.save()
    return render(request, 'restaurant_review/index.html', {'profile': profile})

def lottery(request):
    profile = Profile.objects.get(user=request.user)
    profile.hasLottery = True
    profile.save()
    return render(request, 'restaurant_review/index.html', {'profile': profile})

def surveyOne(request):
    profile = Profile.objects.get(user=request.user)
    profile.survey_one_isComplete = True
    profile.save()
    return render(request, 'restaurant_review/index.html', {'profile': profile})

def surveyTwo(request):
    profile = Profile.objects.get(user=request.user)
    profile.survey_two_isComplete = True
    profile.save()
    return render(request, 'restaurant_review/index.html', {'profile': profile})



# def results(request):
#     # User = get_user_model()
#     all_users = Profile.objects.all()
#     fieldnames = ['experiment_two']
#     fields = [all_users[0]._meta.get_field(field) for field in fieldnames]
#     context = {
#         'rows': all_users,
#         'cols': fields,
#     }
#     return render(request, 'restaurant_review/results.html', context=context)


# def details(request, id):
#     print('Request for restaurant details page received')

#     restaurant = get_object_or_404(Restaurant, pk=id)


#     return render(request, 'restaurant_review/details.html', {'restaurant': restaurant})



# def create_restaurant(request):
#     print('Request for add restaurant page received')

#     return render(request, 'restaurant_review/create_restaurant.html')


# @csrf_exempt
# def add_restaurant(request):
#     try:
#         name = request.POST['restaurant_name']
#         street_address = request.POST['street_address']
#         description = request.POST['description']
#     except (KeyError):
#         # Redisplay the question voting form.
#         return render(request, 'restaurant_review/add_restaurant.html', {
#             'error_message': "You must include a restaurant name, address, and description",
#         })
#     else:
#         restaurant = Restaurant()
#         restaurant.name = name
#         restaurant.street_address = street_address
#         restaurant.description = description
#         Restaurant.save(restaurant)
                
#         return HttpResponseRedirect(reverse('details', args=(restaurant.id,)))


# @csrf_exempt
# def add_review(request, id):
#     restaurant = get_object_or_404(Restaurant, pk=id)
#     try:
#         user_name = request.POST['user_name']
#         rating = request.POST['rating']
#         review_text = request.POST['review_text']
#     except (KeyError):
#         #Redisplay the question voting form.
#         return render(request, 'restaurant_review/add_review.html', {
#             'error_message': "Error adding review",
#         })
#     else:
#         review = Review()
#         review.restaurant = restaurant
#         review.review_date = timezone.now()
#         review.user_name = user_name
#         review.rating = rating
#         review.review_text = review_text
#         Review.save(review)
                
#     return HttpResponseRedirect(reverse('details', args=(id,)))        