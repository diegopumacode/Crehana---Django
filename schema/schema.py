import graphene
from courses.schema import CoursesPaginatedType,CoursesType,FilterItemsType
from graphene_django import DjangoObjectType
from courses.models import Course,Category,Level
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from graphql_auth import mutations

from graphql_auth.schema import UserQuery,MeQuery
import graphql_jwt.utils as jwt_utils

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()

class Query(UserQuery,MeQuery,graphene.ObjectType):
    courses = graphene.Field(CoursesPaginatedType,numItems=graphene.Int(),page=graphene.Int(),category=graphene.String(),sub_category=graphene.String(),level=graphene.String())
    course = graphene.Field(CoursesType, id = graphene.String())
    filterItems = graphene.Field(FilterItemsType)

    def resolve_filterItems(self,info):
        categories = Category.objects.all()
        levels = Level.objects.all()
        return {"categories":categories,"levels":levels}

    def resolve_courses(self,info,numItems =3, page=1,category = None,sub_category = None,level=None):
        courses_by_category = Course.objects.filter(category_id=category) if (category and int(category) is not 0) else Course.objects.all()
        courses_by_subcategory = courses_by_category.filter(sub_category_id=sub_category) if (sub_category and int(sub_category) is not 0) else courses_by_category
        courses_by_level = courses_by_subcategory.filter(level_id=level) if (level and int(level) is not 0) else courses_by_subcategory
     
        pag = Paginator(courses_by_level, numItems)
        page_obj = pag.page(page)
        data = CoursesPaginatedType(
            page=page_obj.number,
            pages=pag.num_pages,
            has_next=page_obj.has_next(),
            has_prev=page_obj.has_previous(),
            objects=page_obj.object_list,
        )
        return data
    
    def resolve_course(self,info,id="0"):
        return Course.objects.get(id=id)

class Mutation(AuthMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query, mutation=Mutation)

