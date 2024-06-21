document.addEventListener('DOMContentLoaded', function() {

    // Handle flash messages close button
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
      alert.querySelector('.close').addEventListener('click', () => {
        alert.classList.add('fade-out');
        setTimeout(() => {
          alert.style.display = 'none';
        }, 500);
      });
    });
  
    // Example function to handle edit button click
    const editButtons = document.querySelectorAll('.btn-primary');
    editButtons.forEach(button => {
      button.addEventListener('click', function(event) {
        event.preventDefault();
        const userId = this.getAttribute('href').split('/').pop();
        // Perform AJAX request to get user data (example)
        console.log(`Edit user with ID: ${userId}`);
        // Implement AJAX request to fetch and display user data in a modal or separate page
      });
    });
  
    // Example function to handle delete button click
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
      button.addEventListener('click', function(event) {
        event.preventDefault();
        const userId = this.getAttribute('href').split('/').pop();
        if (confirm('Are you sure you want to delete this user?')) {
          // Perform AJAX request to delete user (example)
          console.log(`Delete user with ID: ${userId}`);
          // Implement AJAX request to delete user and remove row from table
        }
      });
    });
  
    // Additional functionalities can be added here
  });
  