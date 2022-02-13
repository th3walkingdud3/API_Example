<a href="https://github.com/th3walkingdud3/API_Example/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/th3walkingdud3/API_Example"></a>    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/th3walkingdud3/API_Example/API%20Demo%20Build">

Pull this repo

The `jupyter` folder has the notebook used to create the model and export it.

The `docker` folder has the Dockerfile needed to build the container that will serve the api that uses the model.

(or you can pull the container I built by running `docker pull ghcr.io/th3walkingdud3/api_example:latest` from command line)

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

FastAPI uses the OpenAPI standard, and automatically created the interactive documentation for your API, see image below from `http://127.0.0.1:8000/docs`

<img width="1333" alt="Screen Shot 2022-01-29 at 10 49 31 PM copy" src="https://user-images.githubusercontent.com/2783715/151686009-1b1f9837-418e-4925-af70-e5e619902c8d.png">

The blue boxes tell you the REST method used to interact with each endpoint of the API. Click on the `ad_buy` box:

<img width="1333" alt="Screen Shot 2022-01-29 at 10 49 31 PM" src="https://user-images.githubusercontent.com/2783715/151686062-ec591c00-6d53-40c7-92a6-472953c0cb24.png">

Now you can see the docstring I wrote for that endpoint, followed by the parameters that the endpoing accepts. As the model being served is a linear regression model that estimates units of a product sold for a given combination of TV advertising spend and Radio advertising spend, the endpoint requires those two inputs in order to return a prediction. 

If you look at the `main.py` file in the docker folder, you will see that the enpoint is calling `model.predict([[tv_buy, radio_buy]])`

You can click the `Try it out` button to test the API using the interactive documentation:

<img width="1332" alt="Screen Shot 2022-01-29 at 10 49 54 PM" src="https://user-images.githubusercontent.com/2783715/151686071-ac1217de-dd4c-4503-8b14-f5668c562b9d.png">

Enter values integer values in the available fields and click `Execute` then scroll down.

<img width="1322" alt="Screen Shot 2022-01-29 at 10 50 56 PM" src="https://user-images.githubusercontent.com/2783715/151686208-a4554f1c-027d-421e-a62a-1895b1c8d464.png">

Now you can see the exact command that was sent behind the scenes: 
`curl -X 'GET' \
  'http://127.0.0.1:8000/ad_buy/?tv_buy=400&radio_buy=300' \
  -H 'accept: text/html'`
  
  And you can see the URL alone:
  `http://127.0.0.1:8000/ad_buy/?tv_buy=400&radio_buy=300`
  
  If you copy and paste that url into a new window, you will see the responce in your browser, you can also change the integer values to see how it changes the prediction.
  
  You can also scroll down on the docs page to see what the output is:
  
<img width="1282" alt="Screen Shot 2022-01-29 at 11 07 37 PM" src="https://user-images.githubusercontent.com/2783715/151686238-08cc30a3-1865-48aa-8090-df5f032c52ba.png">
