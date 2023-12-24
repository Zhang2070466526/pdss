from employeePersonnel.section.methods import *


def section_every_week(request):
    sec = Section(request)
    sec.add_meth()
    res = sec.method_center('section_every_week')
    return res


def section_every_month(request):
    sec = Section(request)
    sec.add_meth()
    res = sec.method_center('section_every_month')
    return res
