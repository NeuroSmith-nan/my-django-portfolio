from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet
from .views import SkillViewSet
from .views import ProjectViewSet

router_EP = DefaultRouter()
router_EP.register(r'experience',ExperienceViewSet)

router_SK = DefaultRouter()
router_SK.register(r'skill',SkillViewSet)


router_PJ = DefaultRouter()
router_PJ.register(r'project',ProjectViewSet)

urlpatterns = router_EP.urls + router_SK.urls + router_PJ.urls


