import os

import coverage


covstart = os.environ.get("COVERAGE_PROCESS_START")
if covstart is not None:
    coverage.process_startup()
