from django.shortcuts import render

# Create your views here.

from .models import Topic

def index(request):
    """The home page for Blogs app."""
    return render(request, 'blogs_app/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'blogs_app/topics.html',context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'blogs_app/topic.html',context)