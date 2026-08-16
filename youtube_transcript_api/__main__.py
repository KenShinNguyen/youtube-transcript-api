import sys

import logging

from ._cli import YouTubeTranscriptCli


def main() -> int:
    logging.basicConfig()

    cli = YouTubeTranscriptCli(sys.argv[1:])
    print(cli.run())

    # Exiting with a non-zero status when a video could not be retrieved allows
    # this command to be used in scripts, which would otherwise have no way of
    # telling a failure apart from a successful run.
    return 1 if cli.exceptions else 0


if __name__ == "__main__":
    sys.exit(main())
