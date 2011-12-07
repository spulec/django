"""
Django Unit Test and Doctest framework.
"""

from django.test.client import Client, RequestFactory
from django.test.testcases import (TestCase, TransactionTestCase,
        SimpleTestCase, skipIfDBFeature, skipUnlessDBFeature)
from django.test.utils import Approximate
