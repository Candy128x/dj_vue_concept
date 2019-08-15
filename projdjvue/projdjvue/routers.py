from rest_framework import routers
from article.views import ArticleView
# from employee.views import EmpInfoView


router = routers.DefaultRouter()

router.register(r'article', ArticleView)
# router.extend(r'emp', EmpInfoView)