from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexHtml.as_view(), name='homepage'),

    path('lessons/backend/', ShowBackend.as_view(), name='backend'),

    path('add-lesson/', CreateLesson.as_view(), name='add-lesson'),
    path('super/approval/', ShowOnApproval.as_view(), name='approval'),

    path('super/approval/id<int:lesson_pk>-d<int:decide>', approval_decide, name='approval_decide'),

    path('post/change_bookmarks/', change_bookmarks, name='change_bookmarks'),
]
