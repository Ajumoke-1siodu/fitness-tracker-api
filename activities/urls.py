from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ActivityViewSet
from .metrics import ActivitySummaryView   # import the summary view

router = DefaultRouter()
router.register("activities", ActivityViewSet, basename="activity")

urlpatterns = router.urls + [
    path("activities/summary/", ActivitySummaryView.as_view(), name="activity-summary"),
]

