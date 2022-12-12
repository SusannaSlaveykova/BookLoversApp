from django.shortcuts import redirect


class OwnerRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().user_id != self.request.user.id:
            return redirect("no permission")
        return super().dispatch(request, *args, **kwargs)


class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != self.request.user.id:
            return redirect("no permission")
        return super().dispatch(request, *args, **kwargs)