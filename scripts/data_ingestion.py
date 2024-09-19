import os
from google.cloud import pubsub_v1

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Projects/username/service-account.json" #Edit to not share real path

def receive_messages(project_id, subscription_id):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    def callback(message):
        print(f"Received message: {message.data}")
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...")

if __name__ == "__main__":
    receive_messages("prediction_project", "sub-pr66679")