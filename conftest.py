"""Global fixtures shared across tests."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

from helpers.data_reader import read_json_file

ROOT_DIR = Path(__file__).resolve().parent
DATA_FILE = ROOT_DIR / "data" / "test_data.json"
ENV_FILE = ROOT_DIR / ".env"


@pytest.fixture(scope="session", autouse=True)
def load_environment() -> None:
    """Load environment variables from .env once per test session."""
    load_dotenv(dotenv_path=ENV_FILE, override=False)


@pytest.fixture(scope="session")
def env_config() -> dict:
    """Expose key environment values used by tests."""
    return {
        "base_url": os.getenv("BASE_URL", ""),
        "username": os.getenv("APP_USERNAME", ""),
        "password": os.getenv("APP_PASSWORD", ""),
    }


@pytest.fixture(scope="session")
def all_test_data() -> dict:
    """Load the complete JSON test data file."""
    return read_json_file(DATA_FILE)


@pytest.fixture
def test_case_id(request: pytest.FixtureRequest, record_property) -> str:
    """Return the tagged test case id and attach it to reports."""
    marker = request.node.get_closest_marker("test_case_id")
    case_id = marker.args[0] if marker and marker.args else ""
    record_property("test_case_id", case_id)
    return case_id


@pytest.fixture
def case_data(test_case_id: str, all_test_data: dict) -> dict:
    """Return JSON data matching the current test's case id."""
    if not test_case_id:
        return {}
    return all_test_data.get(test_case_id, {})


@pytest.fixture
def get_test_data(all_test_data: dict):
    """
    Return a callable to fetch test data by case id.

    Usage:
        test_data = get_test_data("PORTAL-T3625")
        test_data = get_test_data("PORTAL-T3625", custom_data_file)
    """

    def _get_test_data(test_case_id: str, test_data_path: str | Path | None = None) -> dict:
        data_source = all_test_data
        if test_data_path:
            path_obj = Path(test_data_path)
            if not path_obj.is_absolute():
                path_obj = ROOT_DIR / path_obj
            data_source = read_json_file(path_obj)
        return data_source.get(test_case_id, {})

    return _get_test_data


@pytest.fixture
def test_data_path() -> Path:
    """Provide default path for primary test data JSON."""
    return DATA_FILE


@pytest.fixture
def key_id(request: pytest.FixtureRequest, record_property) -> str:
    """Extract key marker id, for example: @pytest.mark.key(id='PORTAL-T3625')."""
    marker = request.node.get_closest_marker("key")
    marker_id = marker.kwargs.get("id", "") if marker else ""
    record_property("key_id", marker_id)
    return marker_id


