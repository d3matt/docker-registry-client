from __future__ import absolute_import
from io import BytesIO

from docker_registry_client._BaseClient import (
    BaseClientV1, BaseClientV2, _Manifest
)
from drc_test_utils.mock_registry import (
    mock_v1_registry, mock_v2_registry, TEST_NAME, TEST_TAG,
)


class TestBaseClientV1(object):
    def test_check_status(self):
        url = mock_v1_registry()
        BaseClientV1(url).check_status()


class TestBaseClientV2(object):
    def test_check_status(self):
        url = mock_v2_registry()
        BaseClientV2(url).check_status()

    def test_get_manifest_and_digest(self):
        url = mock_v2_registry()
        manifest, digest = BaseClientV2(url).get_manifest_and_digest(TEST_NAME,
                                                                     TEST_TAG)


class TestManifest(object):
    FAKE_MANIFEST = b'{ "schemaVersion": 2 }'
    FAKE_DIGEST = ('sha256:0467ad45d6957ca671e3d219aa5965d4'
                   '7f8621823a80c8e76174bcc1b9a225fd')

    def test_fromfile(self):
        fobj = BytesIO(self.FAKE_MANIFEST)
        manifest = _Manifest.from_file(fobj=fobj)
        assert manifest._digest == self.FAKE_DIGEST
