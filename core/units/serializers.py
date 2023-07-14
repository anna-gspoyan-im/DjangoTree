from rest_framework import serializers
from .models import Units
from django.contrib.auth.models import User


class UnitsSerializer(serializers.ModelSerializer):
    commander = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    subcommander = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(),
                                                      related_name="subcommanders")
    member = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), related_name="members")

    class Meta:
        model = Units
        fields = ['id', 'commander', 'subcommander', 'member', 'is_active', 'acceptable_level_depth',
                  'accessible_units', 'created_at', 'updated_at']
