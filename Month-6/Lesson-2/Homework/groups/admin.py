from django.contrib import admin

from groups.models import GroupModel, SubjectModel, DailySubjectsModel, GradeModel


admin.site.register(GroupModel)

admin.site.register(SubjectModel)

admin.site.register(DailySubjectsModel)

admin.site.register(GradeModel)
