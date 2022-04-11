
from django.contrib import admin
from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/home',views.CustomerIndex.as_view(),name="employee_home"),
    path('accounts/register',views.SignUpView.as_view(),name="signup"),
    path('accounts/login',views.SigninView.as_view(),name="signin"),
    path('accounts/logout',views.signout,name="signout"),
    path('accounts/password/reset',views.PasswordResetView.as_view(),name="password_reset")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
