import os
import re
from typing import Generator, Dict, Any


class LogFormatError(Exception):
    """Custom exception raised when a log entry violates expected formatting."""
    pass


class LogAnalyzer:
    """Parses system logs efficiently using Python stream generators."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        # Matches formats like: [2026-07-08 12:00:00] ERROR: Database connection failed
        self._log_pattern = re.compile(r"^\[.*?\]\s(?P<level>INFO|WARN|ERROR):\s(?P<message>.*)$")

    def _read_lines(self) -> Generator[str, None, None]:
        """Generator to read file lines safely without loading entire file into memory."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Target log file '{self.file_path}' does not exist.")
        
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                yield line.strip()

    def generate_metrics(self) -> Dict[str, Any]:
        """Parses the stream and aggregates status metrics."""
        metrics = {"INFO": 0, "WARN": 0, "ERROR": 0, "malformed_lines": 0}
        error_messages = []

        for line in self._read_lines():
            if not line:
                continue
            
            match = self._log_pattern.match(line)
            if not match:
                metrics["malformed_lines"] += 1
                continue

            level = match.group("level")
            message = match.group("message")
            
            metrics[level] += 1
            if level == "ERROR":
                error_messages.append(message)

        metrics["recent_errors"] = error_messages
        return metrics


# Mock Execution block
if __name__ == "__main__":
    # Create a temporary log file for demonstration purposes
    mock_log = "app.log"
    with open(mock_log, "w") as f:
        f.write("[2026-07-08 10:15:00] INFO: Server started successfully\n")
        f.write("[2026-07-08 10:16:22] WARN: Memory usage exceeding 80%\n")
        f.write("[2026-07-08 10:18:05] ERROR: Connection timed out to DB\n")
        f.write("INVALID LOG LINE HERE\n")

    print(f"Analyzing log file: {mock_log}")
    analyzer = LogAnalyzer(mock_log)
    results = analyzer.generate_metrics()

    print("\n--- Analytics Results ---")
    print(f"Total Info Logs:  {results['INFO']}")
    print(f"Total Warnings:   {results['WARN']}")
    print(f"Total Error Logs: {results['ERROR']}")
    print(f"Malformed Lines skipped: {results['malformed_lines']}")
    print(f"Logged Errors: {results['recent_errors']}")

    # Clean up file
    if os.path.exists(mock_log):
        os.remove(mock_log)