from __future__ import annotations

import os
import sys

from setuptools import find_packages, setup

dependencies = [
    "aiofiles==23.2.1",  # Async IO for files
    "anyio==4.3.0",
    "boto3==1.34.114",  # AWS S3 for DL s3 plugin
    "chiavdf==1.1.4",  # timelord and vdf verification
    "chiabip158==1.5.1",  # bip158-style wallet filters
    "chiapos==2.0.4",  # proof of space
    "clvm==0.9.10",
    "clvm_tools==0.4.9",  # Currying, Program.to, other conveniences
    "gold_rs==0.9.0",
    "chia-rs==0.9.0",
    "clvm-tools-rs==0.1.40",  # Rust implementation of clvm_tools' compiler
    "aiohttp==3.9.4",  # HTTP server for full node rpc
    "aiosqlite==0.20.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==4.1.4",  # Binary data management library
    "colorama==0.4.6",  # Colorizes terminal output
    "colorlog==6.8.2",  # Adds color to logs
    "concurrent-log-handler==0.9.25",  # Concurrently log and rotate logs
    "cryptography==44.0.3",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.14.0",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "importlib-resources==6.4.0",
    "keyring==25.1.0",  # Store keys in MacOS Keychain, Windows Credential Locker
    "PyYAML==6.0.1",  # Used for config file format
    "setproctitle==1.3.3",  # Gives the gold processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "click==8.1.3",  # For the CLI
    "dnspython==2.6.1",  # Query DNS seeds
    "watchdog==4.0.0",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.24",  # dns lib
    "typing-extensions==4.11.0",  # typing backports like Protocol and TypedDict
    "zstd==1.5.5.1",
    "packaging==24.0",
    "psutil==5.9.4",
    "hsms==0.3.1",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build==1.2.1",
    "coverage==7.5.3",
    "diff-cover==9.0.0",
    "pre-commit==3.5.0; python_version < '3.9'",
    "pre-commit==3.7.1; python_version >= '3.9'",
    "py3createtorrent==1.2.0",
    "pylint==3.2.2",
    "pytest==8.1.1",
    "pytest-cov==5.0.0",
    "pytest-mock==3.14.0",
    "pytest-xdist==3.6.1",
    "pyupgrade==3.15.2",
    "twine==5.1.0",
    "isort==5.13.2",
    "flake8==7.0.0",
    "mypy==1.10.0",
    "black==24.4.2",
    "lxml==5.2.2",
    "aiohttp_cors==0.7.0",  # For blackd
    "pyinstaller==6.7.0",
    "types-aiofiles==23.2.0.20240311",
    "types-cryptography==3.3.23.2",
    "types-pyyaml==6.0.12.20240311",
    "types-setuptools==70.0.0.20240524",
]

legacy_keyring_dependencies = [
    "keyrings.cryptfile==1.3.9",
]

kwargs = dict(
    name="gold-blockchain",
    version="2.0.1",
    author="Mariano Sorgente",
    author_email="mariano@glcoin.net",
    description="Gold blockchain full node, farmer, timelord, and wallet.",
    url="https://glcoin.net/",
    license="Apache License",
    python_requires=">=3.8.1, <4",
    keywords="gold blockchain node",
    install_requires=dependencies,
    extras_require={
        "dev": dev_dependencies,
        "upnp": upnp_dependencies,
        "legacy-keyring": legacy_keyring_dependencies,
    },
    packages=find_packages(include=["build_scripts", "chia", "chia.*", "mozilla-ca"]),
    entry_points={
        "console_scripts": [
            "gold = chia.cmds.chia:main",
            "gold_daemon = chia.daemon.server:main",
            "gold_wallet = chia.server.start_wallet:main",
            "gold_full_node = chia.server.start_full_node:main",
            "gold_harvester = chia.server.start_harvester:main",
            "gold_farmer = chia.server.start_farmer:main",
            "gold_introducer = chia.server.start_introducer:main",
            "gold_crawler = chia.seeder.start_crawler:main",
            "gold_seeder = chia.seeder.dns_server:main",
            "gold_timelord = chia.server.start_timelord:main",
            "gold_timelord_launcher = chia.timelord.timelord_launcher:main",
            "gold_full_node_simulator = chia.simulator.start_simulator:main",
            "gold_data_layer = chia.server.start_data_layer:main",
            "gold_data_layer_http = chia.data_layer.data_layer_server:main",
            "gold_data_layer_s3_plugin = chia.data_layer.s3_plugin_service:run_server",
        ]
    },
    package_data={
        "": ["*.clsp", "*.clsp.hex", "*.clvm", "*.clib", "py.typed"],
        "chia._tests.cmds.wallet": ["test_offer.toffer"],
        "chia._tests.farmer_harvester": ["*.json"],
        "chia._tests.tools": ["*.json", "test-blockchain-db.sqlite"],
        "chia._tests.util": ["bip39_test_vectors.json", "clvm_generator.bin", "protocol_messages_bytes-v*"],
        "chia.util": ["initial-*.yaml", "english.txt"],
        "chia.ssl": ["gold_ca.crt", "gold_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/goldcoin-gl/gold-blockchain/",
        "Changelog": "https://github.com/goldcoin-gl/gold-blockchain/blob/main/CHANGELOG.md",
    },
)

if "setup_file" in sys.modules:
    # include dev deps in regular deps when run in snyk
    dependencies.extend(dev_dependencies)

if len(os.environ.get("GOLD_SKIP_SETUP", "")) < 1:
    setup(**kwargs)  # type: ignore
