"""datascience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url ,include
from datascience.core import views

urlpatterns = [
    url(r'^$', views.home , name="home"),
    url(r'^credit/$', views.creditAnalyis ,name="credit-analysis"),
    url(r'^credit/predit/$', views.creditPredict ,name="credit-predit"),
    url(r'^summarize/$',views.summarize,name="summarize"),
    url(r'^ner/$',views.ner,name="ner"),
    url(r'^sentiment/$',views.sentiment,name="sentiment"),
    url(r'^langdetect/$',views.langdetect,name="langdect"),
    url(r'^clv/$',views.clv,name="clv"),
    url(r'^loyalty/$',views.loyalty,name="loyalty"),
    url(r'^churn/$',views.churn,name="churn"),
    url(r'fraud-detection/$',views.fraudDetection , name= "fraud-detection"),
    url(r'contact/$' , views.contact , name="contact"),
    url(r'satisfaction/$' , views.satisfaction , name="satisfaction"),
    url(r'recommender/$' , views.recommender , name="recommender"),
    url(r'recommender/product/$' , views.recommender_product ),
    url(r'claim-predict/$' , views.claim_predict , name="claim_predict" ),
    url(r'click-stream/$' , views.click_stream , name="click_stream" ),
    url(r'clickstream/' , views.click_stream_data , name="click_stream_data" ),
]
