from django.db import models
from cms.models import CMSPlugin, Page
from urlparse import parse_qs, urlparse
from django.utils.translation import ugettext_lazy as _

class HoverImagePlugin(CMSPlugin):
    image = models.ImageField(upload_to=CMSPlugin.get_media_path)
    hover = models.ImageField(upload_to=CMSPlugin.get_media_path)
    url = models.CharField(_("link"), max_length=255, blank=True, null=True,
        help_text=_("If present, clicking on image will take user to link."))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True,
        blank=True, help_text=_("If present, clicking on image will take user \
        to specified page."))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True,
        null=True, help_text=_("Specifies an alternate text for an image, if \
        the image cannot be displayed.<br />Is also used by search engines to \
        classify the image."))
    longdesc = models.CharField(_("long description"), max_length=255,
        blank=True, null=True, help_text=_("When user hovers above picture,\
        this text will appear in a popup."))
