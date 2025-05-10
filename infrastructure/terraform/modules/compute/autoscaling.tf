resource "aws_appautoscaling_target" "quantum_workers" {
  service_namespace  = "ecs"
  resource_id        = "service/${aws_ecs_cluster.hyqcopt.name}/${aws_ecs_service.quantum_worker.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  min_capacity       = 2
  max_capacity       = 50

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }
    target_value = 70
  }
}