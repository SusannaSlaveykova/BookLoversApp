from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from BookLoversApp.accounts.forms import SignUpForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = SignUpForm
    list_display = ['first_name', 'last_name', 'username', 'email', 'gender', 'age', 'profile_picture']
    ordering = ['username']
    list_filter = ['username', 'gender', 'book']
    search_fields = ['username__startswith']
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["first_name"].label = "Input First name:"
        form.base_fields["last_name"].label = "Input Last name:"
        form.base_fields["username"].label = "Username is:"
        form.base_fields["email"].label = "Email is:"
        form.base_fields["gender"].label = "Gender choice:"
        form.base_fields["age"].label = "Age is:"


        return form


    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender',
                    'age',
                    'profile_picture',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
    )

