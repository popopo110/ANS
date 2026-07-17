import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

EXPECTED_TOTAL = 25

EXPECTED_CLIENTS = {
    "192.168.1.12": 11,
    "192.168.1.10": 8,
    "192.168.1.11": 6,
    "192.168.1.09": 3,
    
}

EXPECTED_PAGES = {
    "/": 16,
    "/about": 1,
    "/contact": 2,
    "/products": 3,
}


def test_report_exists():
    """The agent produced a report file."""
    report = json.loads(Path("/app/report.json").read_text())

    assert "total_requests" in report
    assert "clients" in report
    assert "popular_pages" in report

    assert report["total_requests"] == EXPECTED_TOTAL
    assert report["clients"] == EXPECTED_CLIENTS
    assert report["popular_pages"] == EXPECTED_PAGES
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"
