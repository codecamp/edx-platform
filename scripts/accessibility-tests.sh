#!/usr/bin/env bash
set -e

###############################################################################
#
#   accessibility-tests.sh
#
#   Execute the accessibility tests for edx-platform.
#
#   If the optional `DJANGO_VERSION` environment variable is defined, it
#   specifies which version of Django should be installed when running the
#   tests inside a `tox` virtualenv.  If undefined, the tests are run using
#   the currently active Python environment.
#
###############################################################################

# if specified tox environment is supported, prepend paver commands
# with tox env invocation
if [ -z ${TOX_ENV+x} ] || [[ ${TOX_ENV} == 'null' ]]; then
    TOX=""
elif tox -l |grep -q "${TOX_ENV}"; then
    TOX="tox -r -e ${TOX_ENV} --"
else
    echo "${TOX_ENV} is not currently supported. Please review the"
    echo "tox.ini file to see which environments are supported"
    exit 1
fi

echo "Setting up for accessibility tests..."
source scripts/jenkins-common.sh

echo "Running explicit accessibility tests..."
SELENIUM_BROWSER=phantomjs $TOX paver test_a11y

# The settings that we use are installed with the pa11ycrawler module
export SCRAPY_SETTINGS_MODULE='pa11ycrawler.settings'

echo "Running pa11ycrawler against test course..."
$TOX paver pa11ycrawler --fasttest --skip-clean --fetch-course --with-html
