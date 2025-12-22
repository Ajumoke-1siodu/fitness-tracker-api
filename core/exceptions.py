from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        # Unhandled errors: avoid leaking internals
        return Response({"detail": "Server error. Please try again later."}, status=500)

    # Ensure consistent shape
    if isinstance(response.data, list):
        response.data = {"errors": response.data}
    elif "detail" in response.data and not isinstance(response.data["detail"], dict):
        response.data = {"detail": str(response.data["detail"])}

    return response

