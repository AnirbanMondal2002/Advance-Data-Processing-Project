This project implements a scalable, low-latency fraud detection system for e-commerce transactions using Edge AI and cloud-native services. The architecture enables real-time anomaly detection by leveraging machine learning at the edge, ensuring rapid response and reduced cloud dependency.

🚀 Key Features
Real-Time Fraud Detection using ML models deployed on Edge devices.

Edge AI Inference using lightweight models (e.g., XGBoost, Random Forest) for fast decision-making close to the data source.

AWS-Powered Backend: Integrates Amazon Kinesis, AWS Lambda, SageMaker, and DynamoDB for data stream processing and decision logging.

Alert Mechanism: Sends real-time alerts on suspicious activities via Amazon SNS or Lambda triggers.

Scalable Microservices Architecture with Docker & AWS IoT Core for secure device communication.

🧠 Technologies Used
Edge AI Frameworks: TensorFlow Lite / ONNX / sklearn for model optimization

IoT & Streaming: AWS IoT Core, Amazon Kinesis, MQTT

Data Processing & Storage: AWS Lambda, AWS Glue, Amazon S3, DynamoDB

Model Training: Amazon SageMaker (with RandomForest/XGBoost)

Monitoring & Alerts: CloudWatch, Amazon SNS, AWS Lambda

