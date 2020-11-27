
var router1 = [];
var router2 = [];
var router3 = [];
var router4 = [];
var router5 = [];
var router6 = [];
var router7 = [];

var room1 = document.getElementById('Room1').innerHTML;
room1 = JSON.parse(room1);

for (var i = 0; i < room1.length; i ++) {
  router1[i] = room1[i];
}


var y1 = [10,20,10,20,30,40,50,20,40,50];


var router1 = {
  y: router1,
  type: 'box'
};

var trace2 = {
  y: y1,
  type: 'box'
};

var data = [router1, router2, router3, router4, router5, router6, router7];

Plotly.newPlot('myChart', data);

// Grafico 1

