import json


def open_file(json_file_path):
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError as exc:
        print("Error: File not found.", exc)

    except json.JSONDecodeError as exc:
        print("Error: Invalid JSON format.", exc)


def verify_iam_role_policy(json_file_path):
    data = open_file(json_file_path)

    if not isinstance(data, dict):
        return True

    if "PolicyDocument" not in data:
        return True

    policy_document = data["PolicyDocument"]

    if not isinstance(policy_document, dict):
        return True

    if "Statement" not in policy_document:
        return True

    if not isinstance(policy_document["Statement"], list):
        return True

    for element in policy_document["Statement"]:
        if not isinstance(element, dict):
            return True

        if element.get("Resource") == "*":
            return False

    return True