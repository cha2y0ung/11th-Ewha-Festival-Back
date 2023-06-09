from rest_framework import serializers

from .models import Booth, Menu, Image, Comment, Notice, Time
from account.models import User


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'menu', 'price', 'is_soldout']

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'created_at', 'updated_at', 'content']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id', 'created_at', 'updated_at', 'time']

class BoothListSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField(many=True, read_only=True)
    is_liked = serializers.BooleanField(default=False)
    category = serializers.StringRelatedField(many=True, read_only=True)
    notices = NoticeSerializer(many=True, read_only = True)
    times = TimeSerializer(many=True, read_only = True)
    
    class Meta:
        model = Booth

        fields = ['id', 'user', 'day', 'college', 'category', 'name', 'number', 'thumnail', 
                  'opened', 'times', 'hashtag', 'is_liked', 'created_at', 'updated_at', 'notices']
        read_only_fields= ('thumnail', )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'booth', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields= ('booth', 'user', )


class BoothDetailSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(many=True, read_only=True)
    menus = MenuSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    is_liked = serializers.BooleanField(default=False)
    comments = CommentSerializer(many=True, read_only=True)
    notices = NoticeSerializer(many=True, read_only=True)
    times = TimeSerializer(many=True, read_only = True)

    class Meta:
        model = Booth
        fields = ['id', 'user', 'day', 'college', 'category', 'name', 
                  'number', 'thumnail', 'opened', 'times', 'hashtag', 
                  'description', 'images', 'menus', 'is_liked', 'created_at', 'updated_at', 'comments', 'notices']
