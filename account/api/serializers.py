from account.models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = Account
        exclude = ['is_admin','is_active','is_staff','is_superuser','user_permissions']