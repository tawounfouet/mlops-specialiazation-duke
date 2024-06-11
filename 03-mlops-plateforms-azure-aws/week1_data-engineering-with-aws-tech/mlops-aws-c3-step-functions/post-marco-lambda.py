def lambda_handler(event, context):
    # pylint: disable=unused-argument
    if event["name"] == "Polo":
        return "Great Job!"
    return "Keep Trying"
