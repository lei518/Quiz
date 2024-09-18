from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from blood.models import BloodDonationRequest
from accounts.models import CustomUser

@staff_member_required
def admin_dashboard(request):
    users = CustomUser.objects.all()
    requests = BloodDonationRequest.objects.all()
    return render(request, 'admin_dashboard/dashboard.html', {'users': users, 'requests': requests})

@staff_member_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        # update user logic here
        pass
    return render(request, 'admin_dashboard/edit_user.html', {'user': user})

@staff_member_required
def delete_request(request, request_id):
    donation_request = get_object_or_404(BloodDonationRequest, id=request_id)
    donation_request.delete()
    return redirect('admin_dashboard')
from django.shortcuts import render

# Create your views here.
