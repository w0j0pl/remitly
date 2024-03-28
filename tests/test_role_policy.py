from remitly.role_policy import verify_iam_role_policy


def test_default(datadir):
    result = verify_iam_role_policy(datadir / "default.json")
    assert not result


def test_few_statements(datadir):
    result = verify_iam_role_policy(datadir / "few_statements.json")
    assert not result


def test_prefix_asterisks(datadir):
    result = verify_iam_role_policy(datadir / "prefix_asterisks.json")
    assert result


def test_suffix_asterisks(datadir):
    result = verify_iam_role_policy(datadir / "suffix_asterisks.json")
    assert result


def test_middle_asterisks(datadir):
    result = verify_iam_role_policy(datadir / "middle_asterisks.json")
    assert result


def test_few_asterisks(datadir):
    result = verify_iam_role_policy(datadir / "few_asterisks.json")
    assert result


def test_no_resource_field(datadir):
    result = verify_iam_role_policy(datadir / "no_resource_field.json")
    assert result


def test_list_of_resources(datadir):
    result = verify_iam_role_policy(datadir / "list_of_resources.json")
    assert result


def test_incorrect_json(datadir):
    result = verify_iam_role_policy(datadir / "incorrect_json.json")
    assert result
