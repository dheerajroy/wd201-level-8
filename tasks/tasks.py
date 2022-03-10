from datetime import timedelta, datetime
from celery.decorators import periodic_task
from django.core.mail import send_mail
from .models import Task, STATUS_CHOICES
from accounts.models import CustomUser


@periodic_task(run_every=timedelta(minutes=1))
def every_minute():
    users = CustomUser.objects.filter(report_time__lte=datetime.now().time(), last_report_sent__lt=datetime.now().date())
    for user in users:
        tasks_status = {STATUS_CHOICES[i][0]: Task.objects.filter(status=STATUS_CHOICES[i][0], user=user.user).count() for i in range(len(STATUS_CHOICES))}
        email_body = f'''Your Tasks Summary:
        {tasks_status}
            '''
        send_mail('Testing Content', email_body, 'admin@task_manager.com', ['users@task_manager.com'])
