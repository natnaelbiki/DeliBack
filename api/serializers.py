from rest_framework import serializers
from supplier.models import Shop

class ShopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shop
		fields = ['name', 'desc', 'location']