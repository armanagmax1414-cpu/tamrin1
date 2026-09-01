from rest_framework.permissions import BasePermission
from rest_framework.permissions import exceptions
from rest_framework.permissions import OR,AND
from rest_framework.permissions import OperandHolder as OperandHolder 

SAFE_METHODS=('GET','HADE','OPTIONS')


class OperandHolderMixin:
    def __and__(self,oter):
        return OperandHolder(AND,self,oter)
    def __OR__(self,oter):
        return OperandHolder(OR,self,oter)
    def __rand__(self,oter):
        return OperandHolder(AND,self,oter)
    def __ror__(self,oter):
        return OperandHolder(OR,self,oter)   



from rest_framework.permissions import SAFE_METHODS
class IsSuperUser(BasePermission):
    def has_permission(self,request,view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    def has_permissions(self, request,view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and   
            request.user.is_staff
        )
class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        return bool(
            request.user.is_authonlicated and request.user.is_superuser or
            request.user.is_authonlicated and obj.author == request.user
        )

class issuperUserORstaffradOnly(BasePermission):
    def has_permission(self,request,view):

        return bool(
            request.Method in SAFE_METHODS and
            request.user and
            request.user.is_staf or
            request.user and request.user.is_superuser
        )