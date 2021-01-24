"""Omichh middlewate catalog."""
from users.models import Student, Coach
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware
    
    Ensure every user have their profile data complete.
    """
    def __init__(self, get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        # if not request.user.is_anonymous:
        #     if request.path not in [reverse("complete_profile"), reverse("logout")]:
        #         if hasattr(request.user, "coach"):
        #             profile=request.user.coach
        #             if not profile.school or not profile.phone or not profile.omegaup_user or not profile.category:
        #                 return redirect("complete_profile")
        #         elif hasattr(request.user, "student"):
        #             profile=request.user.student
        #             if not profile.coach or not profile.school or not profile.phone_of_tutor or not profile.omegaup_user or not profile.category:
        #                 return redirect("complete_profile")
        response=self.get_response(request)
        return response