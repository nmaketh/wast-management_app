var ctx = document.getElementById('recyclingChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: {% for user in users %}'{{ user.username }}',{% endfor %},
        datasets: [{
            label: 'Total Recycled',
            data: {% for user in users %}{{ user.total_recycled }},{% endfor %},
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});