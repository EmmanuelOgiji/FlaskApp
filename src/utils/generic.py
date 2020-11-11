import base64


def encode_to_base64(message):
    messagebytes = message.encode('ascii')
    base64bytes = base64.b64encode(messagebytes)
    base64message = base64bytes.decode('ascii')
    return base64message
