import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import blango_auth.views
import blog.views
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index, name='index'),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path("accounts/register/",
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name="django_registration_register",),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/v1/", include("blog.api.urls")),
    path("api/v2/", include("blog.api_urls")),
    path("post-table/", blog.views.post_table, name="blog-post-table"),

]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)