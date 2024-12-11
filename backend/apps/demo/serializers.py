from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'author_username']

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='user.username', read_only=True)

    comment_count = serializers.IntegerField(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'author_username', 'comments', 'comment_count']

    def get_comments(self, obj):
        comments = getattr(obj, 'prefetched_comments', [])
        # we only want the first 3 comments
        return CommentSerializer(comments[:3], many=True).data
