#Zachary Donnelly - CS4300 HW2
from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import AuthenticationMiddleware

#logging in specified user - this user information was hard coded into the manage.py from the shell
#ONLY USE FOR TESTING - NOT SECURE
class TestUserMiddleware(AuthenticationMiddleware):
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__(get_response)

    def __call__(self, request):
        #creating test user
        test_user = get_user_model().objects.get(username="test user")

        #log in the user
        request.user = test_user
        return self.get_response(request)