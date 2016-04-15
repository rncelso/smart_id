from rest_framework import serializers

class timeSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	time = serializers.DateTimeField(format = "%m/%d/%y %I:%M:%S %p")
	studentNumber = serializers.IntegerField()