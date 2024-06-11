def lambda_handler(event, context):
    # pylint: disable=unused-argument
    if event["name"] == "Marco":
        return {"name": "Polo"}
    return {"name": "No"}
