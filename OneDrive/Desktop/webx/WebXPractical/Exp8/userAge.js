// AngularJS User Age Input App
var app = angular.module('userAgeApp', []);

app.controller('UserAgeController', function($scope) {
    $scope.title = "AngularJS User Age Input Demo";
    $scope.user = {
        name: "",
        age: null
    };
    
    $scope.getAgeMessage = function() {
        if (!$scope.user.age) {
            return "";
        }
        
        var age = parseInt($scope.user.age);
        
        if (isNaN(age)) {
            return "Please enter a valid age.";
        } else if (age < 0) {
            return "Age cannot be negative.";
        } else if (age < 18) {
            return "You are a minor.";
        } else if (age < 65) {
            return "You are an adult.";
        } else {
            return "You are a senior citizen.";
        }
    };
    
    $scope.resetForm = function() {
        $scope.user.name = "";
        $scope.user.age = null;
    };
});
