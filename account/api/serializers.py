from account.models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = Account
        exclude = ['is_admin','is_active','is_staff','is_superuser','user_permissions']


    def save(self):
        account = Account(email = self.validated_data['email'],username = self.validated_data['username'])
        password = self.validated_data['password']

        account.set_password(password)
        
        account.save()

        return account