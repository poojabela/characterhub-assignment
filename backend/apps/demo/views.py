from django.db.models import Prefetch, Count
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import CursorPagination
from django.db.models.functions import Random
from .models import Post, Comment
from .serializers import PostSerializer

class PostPagination(CursorPagination):
    page_size = 10

    def get_ordering(self, request, queryset, view):
        if request.query_params.get('post_order') == 'random':
            return (Random(),)
        return ('-timestamp',)

class PostViewSet(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        post_order = self.request.query_params.get('post_order', 'latest')
        comment_order = self.request.query_params.get('comment_order', 'latest')

        # Comment ordering
        if comment_order == 'random':
            comments_queryset = Comment.objects.order_by(Random())
        else:
            comments_queryset = Comment.objects.order_by('-timestamp') # Latest by default

        # Prefetch comments
        # No slicing here
        comments_prefetch = Prefetch(
            'comments',
            queryset=comments_queryset,
            to_attr='prefetched_comments'
        )

        # Post queryset
        queryset = Post.objects.select_related('user').prefetch_related(
            comments_prefetch
        ).annotate(
            comment_count=Count('comments')
        )

        # Post ordering
        if post_order == 'random':
            queryset = queryset.order_by(Random())
        else:
            queryset = queryset.order_by('-timestamp') # Latest by default

        return queryset
