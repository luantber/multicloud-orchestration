provider "aws" {
  profile    = "default"
  region     = "us-east-2"
}


provider "google" {
  credentials = file("gcp.json")

  project = "rich-channel-258220"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}