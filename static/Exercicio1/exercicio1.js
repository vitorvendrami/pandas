// Grafico 1

var ctx = document.getElementById('myChart').getContext('2d');
var my_data = document.getElementById('Room1').innerHTML;
my_data = JSON.parse(my_data);

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Router1", "Router2", "Router3","Router4", "Router5", "Router6", "Router7"],
        datasets: [{
            label: 'Room 1 Mean',
            data: [my_data.Router1, my_data.Router2,
                my_data.Router3, my_data.Router4, my_data.Router5, my_data.Router6, my_data.Router7],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

//Grafico2

var ctx2 = document.getElementById('myChart2').getContext('2d');
var Room2 = document.getElementById('Room2').innerHTML;
Room2 = JSON.parse(Room2);

var myChart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ["Router1", "Router2", "Router3","Router4", "Router5", "Router6", "Router7"],
        datasets: [{
            label: 'Room 2 Mean',
            data: [Room2.Router1, Room2.Router2,
                Room2.Router3, Room2.Router4, Room2.Router5, Room2.Router6, Room2.Router7],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

//Grafico3

var ctx3 = document.getElementById('myChart3').getContext('2d');
var Room3 = document.getElementById('Room3').innerHTML;
Room3 = JSON.parse(Room3);

var myChart3 = new Chart(ctx3, {
    type: 'bar',
    data: {
        labels: ["Router1", "Router2", "Router3","Router4", "Router5", "Router6", "Router7"],
        datasets: [{
            label: 'Room 3 Mean',
            data: [Room3.Router1, Room3.Router2,
                Room3.Router3, Room3.Router4, Room3.Router5, Room3.Router6, Room3.Router7],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

//Grafico4

var ctx4 = document.getElementById('myChart4').getContext('2d');
var Room4 = document.getElementById('Room4').innerHTML;
Room4 = JSON.parse(Room4);

var myChart4 = new Chart(ctx4, {
    type: 'bar',
    data: {
        labels: ["Router1", "Router2", "Router3","Router4", "Router5", "Router6", "Router7"],
        datasets: [{
            label: 'Room 4 Mean',
            data: [Room4.Router1, Room4.Router2,
                Room4.Router3, Room4.Router4, Room4.Router5, Room4.Router6, Room4.Router7],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
