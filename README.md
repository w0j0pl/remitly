# remitly

Remitly is a package done as an interview task for Remitly, Inc.

It verifies the input JSON data which is defined as AWS::IAM::Role Policy and return logical false if an input JSON Resource field contains a single asterisk and true in any other case.

## Installation

Install the package dependencies with:

```shell
pip install -r requirements.txt
```

## Usage

You can run the program using (path - path to the JSON file you want to check):

```shell
python -m remitly path
```

And run unit tests using:

```shell
python -m pytest
```

## License

MIT License
