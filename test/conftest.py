import os
import shutil
import tempfile

import pytest

import pyproj


@pytest.fixture(scope="session")
def aoi_data_directory():
    """
    This is to ensure that the ntv2_0.gsb file is actually
    missing for the AOI tests.
    """
    data_dir = pyproj.datadir.get_data_dir()
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_data_dir = os.path.join(tmpdir, "proj")
        shutil.copytree(data_dir, tmp_data_dir)
        try:
            os.remove(os.path.join(str(tmp_data_dir), "ntv2_0.gsb"))
        except OSError:
            pass
        try:
            pyproj.datadir.set_data_dir(str(tmp_data_dir))
            yield
        finally:
            pyproj.datadir.set_data_dir(data_dir)
