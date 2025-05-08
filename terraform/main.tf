resource "aws_instance" "app" {
  ami                    = "ami-097947612b141c026"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public.id
  iam_instance_profile   = "LabInstanceProfile"
  tags = { Name = "${var.project_name}-app" }
}

resource "aws_s3_bucket" "artifacts" {
  bucket = "${var.project_name}-artifacts-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
  byte_length = 4
}

