def get_file_ids_from_thread(client, thread_id):
    """
    Extracts file_ids from the attachments of messages in a thread, if attachments are not empty.

    :param client: The client object used to interact with the API.
    :param thread_id: The ID of the thread to extract messages from.
    :return: A list of file_ids extracted from the attachments of the messages.
    """
    # Get the list of messages from the thread
    messages = [i for i in client.beta.threads.messages.list(thread_id=thread_id)]

    # Extract file_ids from each message's attachments if attachments are not empty
    file_ids = [
        attachment.file_id
        for message in messages
        if message.attachments
        for attachment in message.attachments
    ]
    
    return file_ids

def write_file_to_temp_dir(file_id, output_path, client):
    file_data = client.files.content(file_id)
    file_data_bytes = file_data.read()
    with open(output_path, "wb") as file:
        file.write(file_data_bytes)

