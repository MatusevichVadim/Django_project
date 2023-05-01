from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    # class check if student is enrolled in the course and returns True or False if not
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
