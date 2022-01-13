from rest_framework import serializers
from news.models import Article
import re


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

 #models로 이동
    # def validate_title(self, title):
    #     if len(title) < 3:
    #         raise serializers.ValidationError("3글자 이상")
    #     if not re.search(r"[ㄱ-힣]", title):
    #         raise serializers.ValidationError("한글을 써주세요.")
    #     return title


#필드 공개여부에 대한 결정
# class ArticleAnonymousSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content"]
#
#
# class ArticleGoldMembershipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content", "photo"]
#
#
# class ArticleAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = "__all__"
