from django.views.generic.base import ContextMixin


class UrlMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(UrlMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context
