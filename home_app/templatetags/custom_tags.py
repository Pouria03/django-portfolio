from django import template
from home_app.models import Resume
register = template.Library()

@register.inclusion_tag('tag_templates/portfolio_modal.html')
def modal(id):
    resume = Resume.objects.get(id=id)
    context = {'resume': resume}
    return context