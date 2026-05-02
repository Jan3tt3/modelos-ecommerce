document.addEventListener('DOMContentLoaded', () => {

    fetch('/sales-chart/')
        .then(response => response.json())
        .then(data => {

            const ctx = document
                .getElementById('salesChart')
                .getContext('2d');

            new Chart(ctx, {

                type: 'bar',

                data: {
                    labels: data.labels,

                    datasets: [{
                        label: 'Ventas Totales',

                        data: data.data,

                        borderWidth: 1
                    }]
                },

                options: {
                    responsive: true,

                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }

            });

        });

});