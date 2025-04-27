// AngularJS User Name Input App
var app = angular.module('userNameApp', []);

app.controller('UserNameController', function($scope) {
    $scope.title = "AngularJS User Name Input Demo";
    $scope.user = {
        firstName: "",
        lastName: ""
    };
    
    $scope.resetForm = function() {
        $scope.user.firstName = "";
        $scope.user.lastName = "";
    };
});
