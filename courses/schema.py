import graphene
from graphene_django import DjangoObjectType
from .models import Course,Category,Level
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
 
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class LevelType(DjangoObjectType):
    class Meta:
        model = Level
        fields = ("id","name")


class CoursesType(DjangoObjectType):
    class Meta:
        model = Course
 
class FilterItemsType(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    levels = graphene.List(LevelType)

class CoursesPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(CoursesType)
 
# class Query(graphene.ObjectType):
#     courses = graphene.Field(CoursesPaginatedType,numItems=graphene.Int(),page=graphene.Int(),category=graphene.String(),sub_category=graphene.String(),level=graphene.String())
 
#     def resolve_courses(self,info,numItems = 10, page=1,category = None,sub_category = None,level=None):

#         courses_by_category = Course.objects.filter(category_id=category) if category else Course.objects.all()
#         courses_by_subcategory = courses_by_category.filter(sub_category_id=sub_category) if sub_category else courses_by_category
#         courses_by_level = courses_by_subcategory.filter(level=level) if level else courses_by_subcategory
     
#         pag = Paginator(courses_by_level, numItems)
#         page_obj = pag.page(page)
#         data = CoursesPaginatedType(
#             page=page_obj.number,
#             pages=pag.num_pages,
#             has_next=page_obj.has_next(),
#             has_prev=page_obj.has_previous(),
#             objects=page_obj.object_list,
#         )
#         return data
# schema = graphene.Schema(query= Query)

