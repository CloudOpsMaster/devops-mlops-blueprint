terraform {
  required_version = ">= 1.0"
}

provider "local" {
  # local provider used as placeholder
}

output "placeholder" {
  value = "dev env placeholder"
}
