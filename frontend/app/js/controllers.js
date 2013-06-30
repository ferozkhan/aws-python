'use strict';

/* Controllers */

angular.module('AWS.controllers', []).
  controller('ec2State', [function() {
        $http.jsonp('/ec2_state/', function(state_data){
            $scope.running_instances = state_data.running;
            $scope.pending_instances = state_data.pending;
            $scope.shutting_down_instances = state_data.shutting-down;
            $scope.terminated_instances = state_data.terminated;
            $scope.stopped_instances = state_data.stopped;
            $scope.stopping_instances = state_data.stopping;

        });
  }]);