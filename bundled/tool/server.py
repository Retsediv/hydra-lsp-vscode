import logging
import logging.config
import os
import pathlib
import site
import sys


BUNDLE_DIR = pathlib.Path(__file__).parent.parent
logger = logging.getLogger(__name__)


def update_sys_path(path_to_add: str) -> None:
    """Add given path to `sys.path`."""
    if os.path.isdir(path_to_add):
        # The `site` module adds the directory at the end, if not yet present; we want
        # it to be at the beginning, so that it takes precedence over any other
        # installed versions.
        sys.path.insert(0, path_to_add)

        # Allow development versions of libraries to be imported.
        site.addsitedir(path_to_add)


def main():
    from hydra_lsp.server import server

    logger.warn("Something..")
    server.start_io()


# Start the server.
if __name__ == "__main__":
    # Ensure that we can import LSP libraries, and other bundled libraries.
    # TODO: probaly not needed
    update_sys_path(os.fspath(BUNDLE_DIR / "libs"))
    main()
