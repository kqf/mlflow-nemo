from mlflow.nemo.search import find_run


def test_finds_run():
    find_run("dummy run")
