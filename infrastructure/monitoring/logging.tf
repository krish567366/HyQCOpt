resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/hyqcopt"
  retention_in_days = 14
}

resource "aws_cloudwatch_dashboard" "main" {
  dashboard_name = "hyqcopt-monitoring"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "metric"
        x      = 0
        y      = 0
        width  = 12
        height = 6
        properties = {
          metrics = [
            ["AWS/Lambda", "Invocations", "FunctionName", "hyqcopt-api"],
            [".", "Errors", ".", "."],
            [".", "Duration", ".", "."]
          ]
          period = 300
          stat   = "Sum"
          region = "us-east-1"
          title  = "API Performance"
        }
      }
    ]
  })
}