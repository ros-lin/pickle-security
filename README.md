# Pickle Security
Safely reading contents of pkl files.

Steps:

1. Ensure `docker` daemon is running
2. Execute `run.py`

`run.py` builds a Docker image using the `Dockerfile` file, then creates a Docker container using the image and bind mounts `container`.
The container will execute `container/unpack_file.py`, which safely reads a `pkl` file (using `pickletools`) and unpacks it into a `txt` file in the mounted directory. Both the container and the image are deleted upon successful execution of `run.py`.

`create_sample.py` creates a sample `pkl` file for testing. The filenames in `unpack_file.py` may need to be changed based on the file you want to deserialize.
