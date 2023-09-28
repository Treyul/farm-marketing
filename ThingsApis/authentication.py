from utils.models import Things_UUID
from rest_framework import authentication
from rest_framework import exceptions

class Thing_Auth(authentication.BaseAuthentication):
    def authenticate(self, request):
        
        # get the custom header params
        UUID = request.META.get("X_KEY")
        
        # revoke reuqest if it does not exist
        if not UUID:
            return None
        
        # validate if exists
        try:
            
            Thing = Things_UUID.objects.get(uuid=UUID)
        except Things_UUID.DoesNotExist:
            raise exceptions.AuthenticationFailed("No deployment done")
            
        return (Thing,None)