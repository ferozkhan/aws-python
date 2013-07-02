'use strict';

// Declare app level module which depends on filters, and services
var app = angular.module('AWS', []);

function ctrl($scope, $http){
    //$scope.data = 'Loading...';
    $scope.url = 'http://localhost:8000/ec2_state/?callback=JSON_CALLBACK';
    $http.jsonp($scope.url).success(function(data){
        $scope.terminated = data.terminated;
        $scope.running = data.running;
        $scope.shutting_down = data.shutting_down;
        $scope.stopped = data.stopped;
        $scope.stopping = data.stopping;
    }).error(function(){});
}

