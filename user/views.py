from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdmin
from .serializers import AdminSignupSerializer, AdminLoginSerializer, CustomerSignupSerializer, CustomerLoginSerializer, \
    SalesAgentSignupSerializer, SalesAgentLoginSerializer
from rest_framework import decorators, permissions, response, request, status
from rest_framework.authtoken.models import Token


# API for Admin Signup
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def admin_signup(req: request.Request) -> response.Response:
    """Signup for admins"""
    admin_signup_ser = AdminSignupSerializer(data=req.data)

    # If the request data is valid, save the data
    if admin_signup_ser.is_valid():
        admin_signup_ser.save()
        return response.Response(
            {"Message": f"Successfully registered {admin_signup_ser.validated_data.get('username')}"},
            status=status.HTTP_200_OK
        )

    return response.Response(admin_signup_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# API for Admin Login
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def admin_login(req: request.Request) -> response.Response:
    """Login for admins"""
    admin_login_ser = AdminLoginSerializer(data=req.data)

    # If the request data is valid, save the data
    if admin_login_ser.is_valid():
        user = admin_login_ser.validated_data.get('user')
        # django_login(request, user)

        try:
            token = Token.objects.get_or_create(user=user)
        except Exception:
            return response.Response({"Message": "Admin Login failed."}, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(
            {"auth_token": token[0].key},
            status=status.HTTP_200_OK
        )

    return response.Response(admin_login_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# API for Customer Signup
@decorators.api_view(["POST"])
@decorators.permission_classes([IsAuthenticated, IsAdmin])
def customer_signup(req: request.Request) -> response.Response:
    """Signup for Customers"""
    cust_signup_ser = CustomerSignupSerializer(data=req.data)

    # If the request data is valid, save the data
    if cust_signup_ser.is_valid():
        cust_signup_ser.save()
        return response.Response(
            {"Message": f"Successfully registered {cust_signup_ser.validated_data.get('username')}"},
            status=status.HTTP_200_OK
        )

    return response.Response(cust_signup_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# API for Customer Login
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def customer_login(req: request.Request) -> response.Response:
    """Login for customers"""
    cust_login_ser = CustomerLoginSerializer(data=req.data)

    # If the request data is valid, save the data
    if cust_login_ser.is_valid():
        user = cust_login_ser.validated_data.get('user')

        # TODO: Validate the OTP

        # django_login(request, user)

        try:
            token = Token.objects.get_or_create(user=user)
        except Exception:
            return response.Response({"Message": "Customer Login failed."}, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(
            {"auth_token": token[0].key},
            status=status.HTTP_200_OK
        )

    return response.Response(cust_login_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# API for Sales Agent Signup
@decorators.api_view(["POST"])
@decorators.permission_classes([IsAuthenticated, IsAdmin])
def sales_agent_signup(req: request.Request) -> response.Response:
    """Signup for Sales Agent"""
    sales_agent_ser = SalesAgentSignupSerializer(data=req.data)

    # If the request data is valid, save the data
    if sales_agent_ser.is_valid():
        sales_agent_ser.save()
        return response.Response(
            {"Message": f"Successfully registered {sales_agent_ser.validated_data.get('username')}"},
            status=status.HTTP_200_OK
        )

    return response.Response(sales_agent_ser.errors, status=status.HTTP_400_BAD_REQUEST)


# API for Sales Agent Login
@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def sales_agent_login(req: request.Request) -> response.Response:
    """Login for admins"""
    sales_agent_login_ser = SalesAgentLoginSerializer(data=req.data)

    # If the request data is valid, save the data
    if sales_agent_login_ser.is_valid():
        user = sales_agent_login_ser.validated_data.get('user')
        # django_login(request, user)

        try:
            token = Token.objects.get_or_create(user=user)
        except Exception:
            return response.Response({"Message": "Sales Agent Login failed."}, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(
            {"auth_token": token[0].key},
            status=status.HTTP_200_OK
        )

    return response.Response(sales_agent_login_ser.errors, status=status.HTTP_400_BAD_REQUEST)
