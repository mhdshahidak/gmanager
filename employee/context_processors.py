from ceo.models import Employees
from pm.models import ProjectMembers


def main_context(request):

    employeedata = Employees.objects.get(id=request.user.employee.id)
    meetinglist1 = ProjectMembers.objects.filter(
        team=employeedata, project__status="Waiting for SRS"
    ).count()
    meetinglist2 = ProjectMembers.objects.filter(
        lead=employeedata, project__status="Waiting for SRS"
    ).count()
    meetingcount = int(meetinglist1) + int(meetinglist2)
    return {"domain": request.META["HTTP_HOST"], "meetingcount": meetingcount}
