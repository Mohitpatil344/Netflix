// AngularJS String Uppercase App
var app = angular.module('uppercaseApp', []);

app.controller('UppercaseController', function($scope) {
    $scope.title = "AngularJS Uppercase Filter Demo";
    $scope.userInput = "Hello, AngularJS!";
});
