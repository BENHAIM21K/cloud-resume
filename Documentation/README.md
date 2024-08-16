Cloud Resume Project
This repository contains the source code and infrastructure setup for my Cloud Resume Project. The project showcases a resume website built using HTML and CSS, hosted on AWS. The project integrates various AWS services to enable continuous deployment, secure content delivery, and real-time notifications when the resume is downloaded.

Project Overview
The Cloud Resume Project is a cloud-based deployment of my personal resume website. The website is hosted on AWS and demonstrates skills in cloud architecture, CI/CD pipelines, serverless computing, and content delivery networks.

Architecture

(Replace the path with the actual path to your architecture diagram in the repository)

Components
GitHub Actions: Used to invalidate the CloudFront cache whenever code is committed to this repository.
AWS CodePipeline: Deploys the committed code from GitHub to an S3 bucket.
Amazon S3: Hosts the static website files (HTML, CSS, images).
Amazon CloudFront: Delivers the content globally with low latency and provides HTTPS security.
Amazon Route 53: Manages the DNS and routes traffic to the CloudFront distribution.
Amazon API Gateway: Manages API requests to trigger backend functions.
AWS Lambda: Handles backend processing, such as sending notifications.
Amazon SNS: Sends email notifications when the resume is downloaded.
IAM Roles: Manages permissions for the services to interact securely.
Features
Continuous Deployment: Automated deployment pipeline via AWS CodePipeline.
Cache Invalidation: GitHub Actions invalidate the CloudFront cache to ensure the latest version of the website is delivered to users.
Secure Content Delivery: The website is served globally via CloudFront with HTTPS.
Serverless Notifications: API Gateway triggers a Lambda function that sends an email notification via SNS when the resume is downloaded.