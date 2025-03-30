import os
import pytest
import mlflow


@pytest.fixture(scope="function")
def mlflow_experiment(tmp_path):
    os.environ["MLFLOW_TRACKING_URI"] = f"file://{tmp_path}"
    mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
    experiment_id = mlflow.create_experiment("test-experiment")

    with mlflow.start_run(run_name="test-run-1"):
        mlflow.log_param("param1", 10)

    with mlflow.start_run(run_name="test-run-2"):
        mlflow.log_param("param2", 20)

    # Simulate the multiple runs with the same name
    with mlflow.start_run(run_name="test-run-2"):
        mlflow.log_param("param2", 23)

    yield experiment_id

    # Cleanup
    del os.environ["MLFLOW_TRACKING_URI"]
