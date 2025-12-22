from datetime import date, timedelta
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Activity

class ActivitySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Activity.objects.filter(user=request.user)

        period = request.query_params.get("period")  # "week" | "month" | None
        date_from = request.query_params.get("date_from")
        date_to = request.query_params.get("date_to")

        if period == "week":
           
            start = date.today() - timedelta(days=6)
            qs = qs.filter(date__gte=start, date__lte=date.today())
        elif period == "month":
            today = date.today()
            start = today.replace(day=1)
            qs = qs.filter(date__gte=start, date__lte=today)

        if date_from:
            qs = qs.filter(date__gte=date_from)
        if date_to:
            qs = qs.filter(date__lte=date_to)

        totals = qs.aggregate(
            total_duration=Sum("duration_minutes"),
            total_distance=Sum("distance_km"),
            total_calories=Sum("calories"),
        )

    
        breakdown = request.query_params.get("breakdown") 
        weekly = monthly = None

        if breakdown == "week":
            weekly = (
                qs.values("date")
                .order_by("date")
                .annotate(
                    duration=Sum("duration_minutes"),
                    distance=Sum("distance_km"),
                    calories=Sum("calories"),
                )
            )
        elif breakdown == "month":
            monthly = (
                qs.extra(select={"month": "DATE_TRUNC('month', date)"})  
                .values("month")
                .order_by("month")
                .annotate(
                    duration=Sum("duration_minutes"),
                    distance=Sum("distance_km"),
                    calories=Sum("calories"),
                )
            )

        return Response({
            "totals": {
                "duration_minutes": totals["total_duration"] or 0,
                "distance_km": totals["total_distance"] or 0.0,
                "calories": totals["total_calories"] or 0,
            },
            "weekly_breakdown": list(weekly) if weekly else None,
            "monthly_breakdown": list(monthly) if monthly else None,
        })
`
