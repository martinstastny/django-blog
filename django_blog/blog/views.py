from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Category
from django.db.models import Count

class PostsListView(TemplateView):
    template_name = 'blog_index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = "blog_post_detail.html"

class CategoryList(ListView):
    model = Category
    template_name = 'blog_categories_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.annotate(num_of_posts=Count('post'))

class CategoryDetail(ListView):

    model = Category
    template_name = 'blog_category_detail.html'

    def get_queryset(self, **kwargs):
        self.category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        self.posts = Post.objects.filter(category=self.category)
        return self.posts

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['posts'] = self.posts

        return context