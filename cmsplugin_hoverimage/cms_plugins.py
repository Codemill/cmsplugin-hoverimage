from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import HoverImagePlugin 
from django.utils.translation import ugettext as _

class CMSHoverImagePlugin(CMSPluginBase):
    model = HoverImagePlugin
    name = _("Hover Image")
    render_template = "hoverimage/image.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""

        context.update({
            'picture': instance,
            'hover': instance.hover,
            'link': link,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSHoverImagePlugin)
