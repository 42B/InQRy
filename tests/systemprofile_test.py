import pytest
from system_profile import SystemProfile

class TestSystemProfile:
    def test_empty_profile_instantiation_works(self):
        SystemProfile()
