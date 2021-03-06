from django.urls import path

from . import views

# from tedygram.images.views import (
#     Feed_view,
#     LikeImage_view,
#     CommentOnImage_view,
#     Comment_view,
# )

app_name = "images"

urlpatterns = [
    path("", view=views.Images.as_view(), name="feed"),
    path("<int:image_id>", view=views.ImageDetail.as_view(), name="image_detail"),
    path("<int:image_id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/unlikes/", view=views.UnLikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("<int:image_id>/comments/<int:comment_id>", view=views.ModerateComments.as_view(), name="comment_image"),
    path("comments/<int:image_id>", view=views.Comment.as_view(), name="comment"),
    path("search/", view=views.Search.as_view(), name="search"),

    # path("", view=Feed_view, name="feed"),
    # path("<int:image_id>/likes/", view=LikeImage_view, name="like_image"),
    # path("<int:image_id>/comments/", view=CommentOnImage_view, name="comment_image"),
    # path("comments/<int:image_id>", view=Comment_view, name="comment")
]
