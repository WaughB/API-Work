# test_main.py

import pytest
from unittest.mock import patch, MagicMock
import main
import sys


def test_default_port():
    with patch.object(sys, "argv", ["main.py"]):
        with patch.object(main, "app") as mock_app:
            main.main()
            mock_app.run.assert_called_with(port=12345, debug=True)


def test_custom_port():
    test_port = 5000
    with patch.object(sys, "argv", ["main.py", str(test_port)]):
        with patch.object(main, "app") as mock_app:
            main.main()
            mock_app.run.assert_called_with(port=test_port, debug=True)
