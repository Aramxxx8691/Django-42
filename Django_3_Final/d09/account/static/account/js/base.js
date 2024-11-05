document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const logoutBtn = document.getElementById('logout-btn');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent the form from submitting normally

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // Create a POST request to the login URL
            fetch(loginForm.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    'username': username,
                    'password': password,
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // If login is successful, reload the page
                    window.location.reload();
                } else {
                    // If login failed, set the error message and trigger the toast
                    showToast(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('An unexpected error occurred.');
            });
        });
    }

    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            // Use the injected logoutUrl variable
            fetch(logoutUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // If logout is successful, redirect to home
                    window.location.href = homeUrl;
                } else {
                    // If logout failed, show an error toast
                    showToast(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('An unexpected error occurred.');
            });
        });
    }

    function showToast(message) {
        const toastElement = document.getElementById('login-toast');
        if (toastElement) {
            const toastBody = toastElement.querySelector('.toast-body');
            toastBody.innerText = message;

            const toast = new bootstrap.Toast(toastElement, {
                autohide: true,
                delay: 5000
            });
            toast.show();
        }
    }
});
