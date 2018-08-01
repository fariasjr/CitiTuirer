from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User


class ProfileAccessMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        if not user == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)