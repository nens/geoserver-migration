import logging
import os
import sys

logger = logging.getLogger(__name__)


def datastore_filepaths(basedir):
    """Return paths to all datastore.xml files found in basedir (+subdirs)."""
    for (dirpath, dirnames, filenames) in os.walk(basedir):
        if not 'datastore.xml' in filenames:
            logger.debug("Directory %s doesn't contain a datastore.xml",
                         dirpath)
            continue
        yield os.path.join(dirpath, 'datastore.xml')


def fix_file(filepath):
    """Write out new file with fixed DB host and password."""
    logger.debug("Looking at %s...", filepath)
    changed = False
    lines = open(filepath).readlines()
    output = []
    for line in lines:
        if 'key="passwd"' in line:
            if not '></entry>' in line:  # Password is already empty.
                line = '<entry key="passwd"></entry>'
                logger.debug("Removed password")
                changed = True
        output.append(line)
    if changed:
        logger.info("Fixed %s", filepath)
        open(filepath, 'w').write(''.join(output))


def main():
    """Main method, called when you run the script."""
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(message)s')
    if len(sys.argv) != 2:
        logger.critical("Pass the script one directory")
        sys.exit(1)
    basedir = sys.argv[1]

    for filepath in datastore_filepaths(basedir):
        fix_file(filepath)


if __name__ == '__main__':
    main()
