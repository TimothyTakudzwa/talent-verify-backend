from rest_framework import permissions

class isOwnerOrSuperUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the snippet.
        if request.user.is_superuser:
            return True
        if hasattr(obj, 'company'):
            return obj.company == request.user.company
        return False
    
class canAddorEdit(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        
        # TODO: Write permissions are only allowed to the owner of the snippet.
        if request.method in permissions.SAFE_METHODS and request.user.can_add_or_edit:
            return True
        return False