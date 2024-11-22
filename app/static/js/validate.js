document.getElementById("signupForm").addEventListener("submit", function(e) {
    e.preventDefault(); // Prevent default form submission for validation

    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Client-side validation
    if (!username || !email || !password || !confirmPassword) {
        alert("All fields are required!");
        return;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    if (password.length < 8) {
        alert("Password must be at least 8 characters.");
        return;
    }

    // If validation passes, submit the form manually
    this.submit(); // This will submit the form if everything is validated
});
