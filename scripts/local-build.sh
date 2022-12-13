COMMIT=$(git log -n 1 --pretty=format:"%h")
VERSION="0.0.1+local$COMMIT"
EXAMPLE_CLI_VERSION=$VERSION python3 setup.py sdist bdist_wheel
echo "Local version is ${VERSION}"