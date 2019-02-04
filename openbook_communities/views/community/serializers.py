from django.conf import settings
from rest_framework import serializers

from openbook_communities.models import Community
from openbook_communities.validators import community_name_characters_validator, community_name_exists


class GetCommunitySerializer(serializers.Serializer):
    community_name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                           allow_blank=False,
                                           required=True,
                                           validators=[community_name_characters_validator, community_name_exists])


class DeleteCommunitySerializer(serializers.Serializer):
    community_name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                           allow_blank=False,
                                           required=True,
                                           validators=[community_name_characters_validator, community_name_exists])


class UpdateCommunitySerializer(serializers.Serializer):
    # The name of the community to update
    community_name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                           validators=[community_name_characters_validator, community_name_exists],
                                           required=True)
    type = serializers.ChoiceField(choices=Community.COMMUNITY_TYPES, required=False)
    name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                 validators=[community_name_characters_validator], required=False)
    title = serializers.CharField(max_length=settings.COMMUNITY_TITLE_MAX_LENGTH, required=False)
    description = serializers.CharField(max_length=settings.COMMUNITY_DESCRIPTION_MAX_LENGTH, required=False,
                                        allow_blank=True)
    rules = serializers.CharField(max_length=settings.COMMUNITY_RULES_MAX_LENGTH, required=False, allow_blank=True)
    user_adjective = serializers.CharField(max_length=settings.COMMUNITY_USER_ADJECTIVE_MAX_LENGTH, required=False)
    users_adjective = serializers.CharField(max_length=settings.COMMUNITY_USERS_ADJECTIVE_MAX_LENGTH, required=False)


class UpdateCommunityAvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField(allow_empty_file=False, required=False)
    community_name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                           allow_blank=False,
                                           required=True,
                                           validators=[community_name_characters_validator, community_name_exists])


class UpdateCommunityCoverSerializer(serializers.Serializer):
    cover = serializers.ImageField(allow_empty_file=False, required=False)
    community_name = serializers.CharField(max_length=settings.COMMUNITY_NAME_MAX_LENGTH,
                                           allow_blank=False,
                                           required=True,
                                           validators=[community_name_characters_validator, community_name_exists])


class GetCommunityCommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = (
            'title',
            'name',
            'avatar',
            'cover',
            'members_count',
            'color',
            'description',
            'rules',
            'user_adjective',
            'users_adjective'
        )
