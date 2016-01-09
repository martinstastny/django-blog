from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.PostsListView.as_view(), name="blog_index"),
    url(r'^categories/$', views.CategoryList.as_view(), name="blog_categories_list"),
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryDetail.as_view(), name="blog_category_detail"),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name="blog_post_detail"),
]