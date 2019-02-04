from django.conf import settings
from rest_framework import serializers

from openbook.settings import COLOR_ATTR_MAX_LENGTH
from openbook_common.validators import hex_color_validator
from openbook_communities.models import Community
from openbook_communities.validators import community_name_characters_validator, community_name_not_taken_validator


class CreateCommunitySerializer(serializers.Serializer):
    type = serializers.ChoiceField(allow_blank=False, choices=Community.COMMUNITY_TYPES)
    name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                 allow_blank=False, validators=[community_name_characters_validator])
    title = serializers.CharField(max_length=settings.COMMUNITY_TITLE_MAX_LENGTH,
                                  allow_blank=False)
    description = serializers.CharField(max_length=settings.COMMUNITY_DESCRIPTION_MAX_LENGTH,
                                        allow_blank=True)
    rules = serializers.CharField(max_length=settings.COMMUNITY_RULES_MAX_LENGTH,
                                  allow_blank=True)
    user_adjective = serializers.CharField(max_length=settings.COMMUNITY_USER_ADJECTIVE_MAX_LENGTH,
                                           allow_blank=True)
    users_adjective = serializers.CharField(max_length=settings.COMMUNITY_USERS_ADJECTIVE_MAX_LENGTH,
                                            allow_blank=True)
    avatar = serializers.ImageField(required=False)
    cover = serializers.ImageField(required=False)
    color = serializers.CharField(max_length=COLOR_ATTR_MAX_LENGTH, required=True,
                                  validators=[hex_color_validator])


class CommunityNameCheckSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                 allow_blank=False,
                                 validators=[community_name_characters_validator, community_name_not_taken_validator])


class GetCommunitiesSerializer(serializers.Serializer):
    count = serializers.IntegerField(
        required=False,
        max_value=20
    )
    query = serializers.CharField(
        max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
        allow_blank=False,
        required=True
    )


class GetCommunitiesCommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = (
            'id',
            'name',
            'title',
            'avatar',
            'cover',
            'members_count',
            'color',
            'user_adjective',
            'users_adjective'
        )
