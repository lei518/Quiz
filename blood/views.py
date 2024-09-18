from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .models import BloodDonationRequest
from .forms import BloodDonationRequestForm

class CreateBloodDonationRequest(View):
    def get(self, request):
        form = BloodDonationRequestForm()
        return render(request, 'blood/create_request.html', {'form': form})

    def post(self, request):
        form = BloodDonationRequestForm(request.POST)
        if form.is_valid():
            donation_request = form.save(commit=False)
            donation_request.user = request.user.profile
            donation_request.save()
            return redirect('blood_request_list')
        return render(request, 'blood/create_request.html', {'form': form})

class EditBloodDonationRequest(View):
    def get(self, request, pk):
        donation_request = get_object_or_404(BloodDonationRequest, pk=pk)
        form = BloodDonationRequestForm(instance=donation_request)
        return render(request, 'blood/edit_request.html', {'form': form})

    def post(self, request, pk):
        donation_request = get_object_or_404(BloodDonationRequest, pk=pk)
        form = BloodDonationRequestForm(request.POST, instance=donation_request)
        if form.is_valid():
            form.save()
            return redirect('blood_request_detail', pk=pk)
        return render(request, 'blood/edit_request.html', {'form': form})

class DeleteBloodDonationRequest(View):
    def post(self, request, pk):
        donation_request = get_object_or_404(BloodDonationRequest, pk=pk)
        donation_request.delete()
        return redirect('blood_request_list')

class BloodDonationRequestList(View):
    def get(self, request):
        requests = BloodDonationRequest.objects.all()
        return render(request, 'blood/request_list.html', {'requests': requests})

class BloodDonationRequestDetail(View):
    def get(self, request, pk):
        request_detail = get_object_or_404(BloodDonationRequest, pk=pk)
        return render(request, 'blood/request_detail.html', {'request': request_detail})
