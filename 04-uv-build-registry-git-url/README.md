# Sample Project

# run these commands 

uv --version
podman --version

# build offline
cd ~/uv-tests/04-uv-build-registry-git-url
podman build -f Dockerfile -t uv-build-test --network none . 2>&1

# run, install and verify
podman run -it --rm uv-build-test /bin/bash -c "
uv pip install dist/*.whl --system --verbose &&
python -c \"import click; import flask; import httpx; print('all imports ok')\"
"