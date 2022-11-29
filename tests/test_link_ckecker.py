import pytest
from links_checker import cli
from links_checker.script import links_checker
from typer.testing import CliRunner

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{cli.__app_name__} v{cli.__version__}\n" in result.stdout


test_data1 = {
    'input': ('https://google.com', 'https://www.facebook.com'),
    'output': {
        "https://google.com": {
            "GET": 200,
            "HEAD": 301,
        },
        "https://www.facebook.com": {
            "GET": 200,
            "POST": 200,
            "PUT": 200,
            "PATCH": 200,
            "DELETE": 200,
            "OPTIONS": 200,
            "HEAD": 200,
        }
    }
}
test_data2 = {
    'input': (
        'https:/google.com',
        'https://google',
        'google.com',
        'https://amazon.com'
    ),
    'output': {
        "https://amazon.com": {
            "GET": 503,
            "POST": 503,
            "PUT": 503,
            "PATCH": 503,
            "DELETE": 503,
            "OPTIONS": 503,
            "HEAD": 301,
        }
    }
}
test_data3 = {
    'input': ('google.com',),
    'output': {}
}


@pytest.mark.parametrize(
    'input_data, output_data',
    [
        pytest.param(
            test_data1["input"],
            test_data1["output"]
        ),
        pytest.param(
            test_data2["input"],
            test_data2["output"],
        ),
        pytest.param(
            test_data3["input"],
            test_data3["output"],
        ),
    ],
)
def test_app(input_data, output_data):
    assert links_checker(input_data) == output_data
    assert isinstance(links_checker(input_data), dict)
    result = runner.invoke(cli.app, ['get', *input_data])
    assert result.exit_code == 0
    assert f"{output_data}" in result.stdout
