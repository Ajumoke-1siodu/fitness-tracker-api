from rest_framework import viewsets, permissions 
from rest_framework.filters import OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend 
from .models import Activity 
from .serializers import ActivitySerializer 
from .filters import ActivityFilter

class ActivityViewSet(viewsets.ModelViewSet):
    """ 
    Provides CRUD operations for Activity model: 
    - Create activity 
    - List activities 
    - Retrieve activity 
    - Update activity 
    - Delete activity 
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter] 
    filterset_class = ActivityFilter ordering_fields = ["date", "duration_minutes", "calories", "distance_km"] 
    ordering = ["-date"] # default: newest first
    
    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
#  User CRUD (Profile)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows logged-in user to:
    - View profile (GET)
    - Update profile (PUT/PATCH) 
    - Delete account (DELETE)
    """ 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 
    def get_object(self): 
        # Always return the logged-in user 
        return self.request.user
    
    # User Registration 
    class RegisterView(generics.CreateAPIView): """ Allows new users to register (POST). """ queryset = User.objects.all() serializer_class = UserSerializer permission_classes = [permissions.AllowAny]
# Create your views here.
