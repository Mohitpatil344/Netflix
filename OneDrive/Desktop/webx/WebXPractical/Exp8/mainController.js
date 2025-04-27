// AngularJS Main Controller
var app = angular.module('mainApp', []);

app.controller('MainController', function($scope) {
    $scope.title = "AngularJS Main Controller Demo";
    $scope.message = "This is a simple AngularJS application demonstrating controllers";
    $scope.items = [
        { id: 1, name: "Item 1", price: 10.99 },
        { id: 2, name: "Item 2", price: 5.99 },
        { id: 3, name: "Item 3", price: 7.50 },
        { id: 4, name: "Item 4", price: 12.25 }
    ];
    
    $scope.totalItems = $scope.items.length;
    
    $scope.getTotalPrice = function() {
        var total = 0;
        for (var i = 0; i < $scope.items.length; i++) {
            total += $scope.items[i].price;
        }
        return total;
    };
});
