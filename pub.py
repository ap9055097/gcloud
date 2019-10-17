import os
from google.cloud import pubsub_v1
def hello_world(request):
   request_json = request.get_json()
   if request.args and 'message' in request.args:
       publisher = pubsub_v1.PublisherClient()
       topic_name = 'projects/{project_id}/topics/{topic}'.format(
           project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
           topic='test_message',  # Set this to something appropriate.
       )
       publisher.publish(topic_name, request.args['message'].encode('utf-8'), spam='eggs')
       return 'success'
   else:
       return f'Hello World!'