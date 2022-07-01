# Create your views here.
# Import necessary classes
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Topic

# Create your views here.
def index(request):
    from .models import Topic
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list})
    # response = HttpResponse()
    # heading1 = '<p>' + 'List of topics : ' + '</p>'
    # response.write(heading1)
    # for topic in top_list:
    #     para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
    #     response.write(para)
    #
    # from .models import Course
    # top_list1 = Course.objects.all().order_by('-price')[:5]
    # heading2 = '<p>' + 'List of Courses : ' + '</p>'
    # response.write(heading2)
    # for Course in top_list1:
    #     para = '<p>' + str(Course.name) + ': ' '</p>'
    #     if Course.for_everyone:
    #         para+='<b><li> This Course is for Everyone </li></b>'
    #     else:
    #         para+='<b><li> This Course is not for Everyone </li></b>'
    #     para+='<p> </p>'
    #     response.write(para)
    # return response


def about(request):
    # response = HttpResponse()
    # heading3 = '<p>' + 'This is an E-learning Website! Search our Topics to find all available Courses.' + '</p>'
    # response.write(heading3)
    return render(request, 'myapp/about.html')


def detail(request, top_no):
    from .models import Course
    course = Course.objects.filter(topic__id__contains=top_no)
    return render(request, 'myapp/detail.html', {'course': course})
    # response=HttpResponse()
    # from .models import Topic, Course
    # details = Topic.objects.filter(id__exact=top_no)
    # page=get_object_or_404(Topic,id=top_no)
    # for Category in details:
    #     data = '<p>' 'Category as per Top Number ' +str(top_no) + '<b>' + ' : ' + str(Category.category) + '</b></p>'
    # details = Course.objects.filter(topic_id__exact=top_no)
    # data += '<p> <b>' 'Courses under ' + Category.category +'</b></p>'
    # data+='<ol>'
    # for Courses in details:
    #     data+= '<p><li>' + str(Courses.name) + '</li></p>'
    # data+='</ol>'
    # if top_no==None:
    #     response.write(page)
    # else:
    #     response.write(data)
    # return response
