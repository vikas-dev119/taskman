from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib import messages
from .forms import AddTaskForm
from .models import Task
from activities.models import Activity


class Index(TemplateView):
    def get(self, request):
        user_id = request.session.get('userauth', {}).get('user_id')
        tasks = Task.objects.filter(user_id=user_id).order_by('-created_on')
        return render(request, 'tasks/index.html', {'tasks': tasks} )


class AddTask(TemplateView):
    template_name = 'tasks/add.html'
    form = AddTaskForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form()} )

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            try:
                user_id = request.session.get('userauth', {}).get('user_id')
                task_name = request.POST.get('name')

                data = {
                    'name': task_name,
                    'deadline': request.POST.get('deadline_date'),
                    'user_id': user_id
                }
                task_obj = Task(**data)
                task_obj.save()

                # update activity
                activity_dict = {
                    'user_id': user_id,
                    'message': 'You created Task {}'.format(str(task_name))
                }
                Activity(**activity_dict).save()
                messages.success(request, "Task add successfully !")
                return redirect('task-list')
            except RuntimeWarning:
                return redirect('task-list')
        
        return render(request, self.template_name, {'form': form})


class DeleteTask(TemplateView):
    def get(self, request, task_id):
        user_id = request.session.get('userauth', {}).get('user_id')
        try:
            task_obj = Task.objects.get(id=task_id, user_id=user_id)
            task_name = task_obj.name
            task_obj.delete()
            messages.success(request, "Task Deleted successfully !")

            # update activity
            activity_dict = {
                'user_id': user_id,
                'message': 'You deleted Task {}'.format(str(task_name))
            }
            Activity(**activity_dict).save()
        except Exception as e:
            print(e)

        return redirect ('task-list')


class ChangeStatus(TemplateView):
    def post(self, request):
        status = 'success'
        message = 'Status change successfully !'

        action = request.POST.get('action')
        tasks = request.POST.get('tasks_id')

        task_list = list(tasks.split(","))
        task_list = [int(x) for x in task_list]

        task_status = 0
        if action == 'complete':
            task_status = 1

        try:
            update_data = {'status': task_status}
            Task.objects.filter(id__in=task_list).update(**update_data)
            messages.success(request, message)
        except Exception as e:
            message = str(e)
            status = 'error'

        return JsonResponse({'status':status, 'message':message})        
