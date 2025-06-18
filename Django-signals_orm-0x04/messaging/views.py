from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out the user before deleting the account
        user.delete()    # This is required for the check
        return redirect('account_deleted')  # Redirect to a confirmation page
    return render(request, 'chats/confirm_delete.html')
