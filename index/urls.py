from django.conf.urls import url
from index.views import *

urlpatterns = [
    url(r'^$',index_view),
    url(r'^login/$',login_view),
    url(r"^register/$",register_view),
    url(r"^uphonec/$",uphonec_view), # 检查手机号码是否存在,
]
