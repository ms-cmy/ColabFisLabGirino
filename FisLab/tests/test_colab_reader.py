from unittest.mock import patch
from FisLab.colab_reader import get_filepaths

def test_get_filepaths(tmp_path):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "testfile1.txt").write_text("content")
    (subdir / "testfile2.txt").write_text("content")

    with patch('FisLab.config.GOOGLE_BASE_PATH', str(tmp_path)):
        str_tmp_path = str(tmp_path)
        expected = [str(subdir / "testfile1.txt"), str(subdir / "testfile2.txt")]
        file_paths = [i for i in get_filepaths(str_tmp_path.rsplit("/", 1)[0]) if i.endswith(".txt")]
        assert sorted(file_paths) == sorted(expected)
