import pytest
from wagtail.contrib.redirects import tmp_storages

@pytest.fixture
def storage():
    s = tmp_storages.CacheStorage(name="my_file")
    s.CACHE_PREFIX = "prefix_"
    return s

def test_remove_cache_with_prefix(storage, monkeypatch):
    from unittest.mock import Mock
    cache_mock = Mock()
    monkeypatch.setattr("wagtail.contrib.redirects.tmp_storages.cache", cache_mock)
    
    storage.remove()

    cache_mock.delete.assert_called_once_with("prefix_my_file")

