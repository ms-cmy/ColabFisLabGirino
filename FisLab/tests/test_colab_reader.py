import pytest
from unittest.mock import patch
from FisLab.colab_reader import get_filepaths

def test_get_filepaths(tmp_path):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "testfile1.txt").write_text("content")
    (subdir / "testfile2.txt").write_text("content")

    with patch('FisLab.colab_reader.GOOGLE_BASE_PATH', str(tmp_path)):
        expected = [str(subdir / "testfile1.txt"), str(subdir / "testfile2.txt")]
        assert sorted(get_filepaths("subdir")) == sorted(expected)
