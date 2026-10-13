# Contact-Feedback-Application-using-AWS
Lambda–SNS End-to-End Project
Contact / Feedback Application using AWS
An end-to-end serverless Contact/Feedback application built with AWS services. Users submit their name, email, and message through a static website hosted on Amazon S3. The request is handled by Amazon API Gateway and AWS Lambda, stored in Amazon DynamoDB, and a notification is published through Amazon SNS to send an email alert.
Architecture
IAM → S3 Website → API Gateway → Lambda → DynamoDB → SNS → Email Notification
1. A user opens the static website hosted on Amazon S3.
2. The user enters their name, email address, and message in the contact form.
3. The website sends an HTTP POST request to Amazon API Gateway.
4. API Gateway invokes the AWS Lambda function.
5. Lambda validates the submitted data and stores the message in DynamoDB.
6. Lambda publishes a notification to an Amazon SNS topic.
7. SNS sends an email notification to the subscribed email address.
Note: IAM provides the permissions required for Lambda and other AWS services to interact securely. S3 hosts the website; DynamoDB stores submissions; SNS sends notifications.

AWS Services Used
Service	Purpose
Amazon S3	Hosts the static website files
Amazon API Gateway	Provides the HTTP endpoint for form submissions
AWS Lambda	Processes and validates contact form submissions
Amazon DynamoDB	Stores contact/feedback records
Amazon SNS	Publishes email notifications
AWS IAM	Manages roles and permissions between AWS services
Amazon CloudWatch	Stores Lambda logs and helps troubleshoot errors


Features
- Serverless architecture; no server management required
- Static website hosting on Amazon S3
- HTTP API endpoint for contact form submissions
- Input validation in Lambda
- Persistent message storage in DynamoDB
- Email notifications through Amazon SNS
- Logging and troubleshooting through CloudWatch
- IAM-based access control
Project Structure
Example structure (adjust filenames to match your repository):
Lambda-SNS-end-to-end-project/
├── website/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── lambda/
│   └── lambda_function.py
├── screenshots/
└── README.md
Prerequisites
- An AWS account
- Basic knowledge of AWS IAM, Lambda, API Gateway, DynamoDB, SNS, and S3
- A verified email address for the SNS subscription
- A web browser and curl or Postman for testing
Setup Guide
1. Create an SNS topic
1. Open the Amazon SNS console.
2. Create a Standard topic, for example ContactNotifications.
3. Create an email subscription to the topic.
4. Open the confirmation email and confirm the subscription.
5. Keep the topic ARN for the Lambda configuration.
SNS email notifications will not arrive until the subscription is confirmed.
2. Create a DynamoDB table
1. Open Amazon DynamoDB.
2. Create a table, for example ContactMessages.
3. Choose a partition key that matches the Lambda code, such as messageId (String).
4. Keep the table name and Region available for Lambda configuration.
Make sure the table's key schema matches the attributes written by your Lambda function.
3. Create the Lambda function and IAM role
1. Create a Lambda function, for example ContactAppFunction.
2. Choose a runtime supported by your code.
3. Create or assign an execution role with least-privilege permissions.
4. Grant the function permission to:
   - Write items to the specified DynamoDB table.
   - Publish messages to the specified SNS topic.
   - Write logs to CloudWatch Logs.
5. Configure the table name and SNS topic ARN as environment variables if your code uses them.
6. Deploy your Lambda code.
Do not place AWS access keys or other secrets directly in the source code. Use an IAM execution role.
4. Create the API Gateway route
1. Open Amazon API Gateway and create or select your API.
2. Create a POST route that matches the path used by the website, for example /Contact or /contact.
3. Integrate the route with ContactAppFunction.
4. Allow API Gateway to invoke the Lambda function.
5. Configure CORS if the browser-based website needs to call the API from a different origin.
6. Deploy the API to a stage, or use the $default stage where appropriate.
7. Copy the deployed Invoke URL.
Important: Route paths are case-sensitive. The route path, stage, and URL used by the website and test commands must match exactly.
5. Host the website on S3
1. Create an S3 bucket for the website.
2. Upload the website files (index.html, CSS, and JavaScript).
3. Enable static website hosting if you are using the S3 website endpoint.
4. Configure the website's JavaScript to send a POST request to your API Gateway endpoint.
5. Configure API Gateway CORS to allow the website's exact origin, the POST method, and required headers such as content-type.
6. Open the website endpoint and test the form.
For production use, consider serving the site through Amazon CloudFront with HTTPS and an appropriate access configuration. Avoid making an S3 bucket public unless that is intentionally required for your hosting design.
6. Connect and test the full workflow
Submit a test message through the website. Verify that:
- API Gateway receives the request.
- Lambda executes without errors.
- The message appears in DynamoDB.
- SNS publishes a notification.
- The subscribed email inbox receives the notification.
- CloudWatch Logs show the Lambda execution details.
Test the API with curl
Replace the example URL with your actual deployed API URL. The path and stage must match your API Gateway configuration.
Windows Command Prompt (CMD)
curl -X POST "https://YOUR_API_ID.execute-api.ap-south-1.amazonaws.com/YOUR_STAGE/Contact" -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"email\":\"alice@example.com\",\"message\":\"Testing API Gateway\"}"
If you use the $default stage, the stage segment is generally omitted. If your route is /contact in lowercase, replace /Contact with /contact. Do not include YOUR_STAGE literally; replace it with the real stage name or remove that segment when appropriate.
A successful response depends on how the Lambda function is written. Check the API response, DynamoDB table, SNS subscription, and CloudWatch Logs to verify the full workflow.
Troubleshooting
Problem	What to check
{"message":"Not Found"}	Verify the route path, capitalization, stage, Invoke URL, and deployment
403 Forbidden	Check API authorization, resource policies, and permissions
500 Internal Server Error	Check Lambda errors and CloudWatch Logs
Browser shows Failed to fetch	Check API Gateway CORS settings, the website origin, endpoint URL, and browser console
No DynamoDB record	Check Lambda execution role, table name, Region, key schema, and logs
No SNS email	Confirm the SNS email subscription, topic ARN, Lambda publish permission, and spam folder


Security Best Practices
- Follow least-privilege IAM permissions.
- Restrict Lambda access to only the required DynamoDB table and SNS topic.
- Do not commit access keys, passwords, tokens, or sensitive configuration to GitHub.
- Validate all user input in Lambda.
- Configure CORS for trusted website origins instead of allowing every origin when possible.
- Monitor errors with CloudWatch Logs and metrics.
- Consider rate limiting and request validation to reduce unwanted submissions.
- Do not store unnecessary personal information.
Learning Outcomes
By completing this project, you can practice:
- Building a serverless AWS application
- Connecting API Gateway to Lambda
- Using IAM roles and permissions
- Saving application data in DynamoDB
- Sending email notifications through SNS
- Hosting static websites on S3
- Configuring CORS and debugging HTTP requests
- Monitoring Lambda with CloudWatch
Future Improvements
- Add CAPTCHA or another anti-spam mechanism.
- Add stronger validation and abuse protection.
- Use CloudFront and HTTPS for website delivery.
- Add automated tests and infrastructure as code using AWS SAM, AWS CDK, or Terraform.
- Add a status field and an administrative view for feedback records.
  

Author
Mohd Maaz
Computer Science Graduate | AWS | Linux | DevOps | Cloud Computing
