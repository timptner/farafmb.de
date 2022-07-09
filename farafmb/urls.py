from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path, reverse
from oauth2_provider.views import ConnectDiscoveryInfoView


def redirect_admin(request):
    base_url = reverse('login')
    if 'next' in request.GET:
        url = f"{base_url}?next={request.GET.get('next')}"
    else:
        url = base_url
    return redirect(url)


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/login/', redirect_admin),
    path('admin/', admin.site.urls),

    path('i18n/', include('django.conf.urls.i18n')),

    re_path(r'^oauth/\.well-known/openid-configuration/?$',
            ConnectDiscoveryInfoView.as_view(),
            name='oidc-connect-discovery-info'),  # Serve discovery view on both routes
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

urlpatterns += i18n_patterns(
    path('', include('blog.urls')),
    path('about/', include('about.urls')),
    path('consultations/', include('consultations.urls')),
    path('documents/', include('documents.urls')),
    path('events/', include('events.urls')),
    path('exams/', include('exams.urls')),
    path('excursions/', include('excursions.urls')),
    path('jobs/', include('jobs.urls')),
    path('links/', include('links.urls')),
    path('meetings/', include('meetings.urls')),
    path('members/', include('members.urls')),
    path('mentoring/', include('mentoring.urls')),

    prefix_default_language=False
)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
