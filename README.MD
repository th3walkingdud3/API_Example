Pull this repo

The `jupyter` folder has the notebook used to create the model and export it.

The `docker` folder has the Dockerfile needed to build the container that will serve the api that uses the model.

On the command line, navigate to the 'docker' folder and build the docker image:
`docker build -t apitest:latest .`   
Make sure you include the period at the end of the command above.

Once the build is complete, find the image id:

`docker image ls -a'

You should see something like this:

| REPOSITORY                   | TAG                   | IMAGE ID       | CREATED          | SIZE  |
| ---------------------------- | --------------------- | -------------- | ---------------- | ----- |
| apitest                      | latest                | abbfe255f4f5   | 27 minutes ago   | 665MB |


Copy the image id and run:

`docker run -p 8000:8000 abbfe255f4f5`

Note that the image id in the command above matches the output from docker image ls command. Make sure yours does as well.


Now open a web browser and navigate to `http://127.0.0.1:8000/`

