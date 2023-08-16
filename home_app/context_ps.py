from home_app.models import GeneralSiteInfo


def get_general_site_info(request):
    general_site_info = GeneralSiteInfo.objects.last()
    return {
        'site_info': general_site_info
    }