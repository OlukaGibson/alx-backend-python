#!/usr/bin/env python3
"""
Unit and integration tests for client.py
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class

# Define TEST_PAYLOAD here to avoid import errors and index errors
TEST_PAYLOAD = [
    {
        "repos_url": "https://api.github.com/orgs/google/repos"
    },
    [
        {"name": "rails", "license": {"key": "mit"}},
        {"name": "django", "license": {"key": "apache-2.0"}},
    ],
]


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns expected value from org payload"""
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = TEST_PAYLOAD[0]
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                TEST_PAYLOAD[0]["repos_url"]
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns list of repo names"""
        mock_get_json.return_value = TEST_PAYLOAD[1]

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = TEST_PAYLOAD[0]["repos_url"]
            client = GithubOrgClient("google")
            expected_repos = [repo["name"] for repo in TEST_PAYLOAD[1]]
            self.assertEqual(client.public_repos(), expected_repos)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns correct boolean"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (
            TEST_PAYLOAD[0],
            TEST_PAYLOAD[1],
            ["rails", "django"],
            ["django"],
        ),
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests using fixtures"""

    @classmethod
    def setUpClass(cls):
        """Patch get_json before tests"""
        cls.get_patcher = patch(
            "client.get_json",
            side_effect=[cls.org_payload, cls.repos_payload]
        )
        cls.mock_get_json = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop patcher after tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repo names"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filtering"""
        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)
