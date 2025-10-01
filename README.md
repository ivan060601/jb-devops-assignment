## Basic application description

The application itself is a simple Python-based webserver with following endpoints available:

- `/healthCheck` - an endpoint used by k8s to compute a health probe, returns 200OK if the webserver is up and running 
- `/healthCheckButBroken` - an endpoint that always returns 500 error, useful while testing the ci/cd logic
- `/**` - basically any other endpoint, will return a simple HTML page with a predefined greeting
## Build & Run locally

In order to build an image of this app locally, you can use a Dockerfile provided by this repo and simply run a following command:
```bash
docker build -t simple-app:{TAG} .
```
Where `TAG` is a valid image tag you like, e.g. `v1`

After building the image, you can run it locally:
```bash
docker run -d --rm -p 8080:8080 --name=simple-app simple-app:{TAG}
```

You will find your freshly-built app by the following URL: `http://localhost:8080`

## Deploy

### Deploy to dev

In order to create a dedicated dev-environment you can simply checkout to you own branch and push the changes back to this repo.
It will create a new env for you with a following name: `https://{YOUR_BRANCH_NAME}.jb-assignment.shakhtarov.me`

> [!WARNING]
> Please do not use an underscore in a branch name since it is not a valid URL-symbol. It will probably fail your deploy job.

### Deploy to stage

After changes are stabilized, they are merged or rebased into the `main` branch. This automatically triggers a pipeline to build, deploy and test a new code on the `https://stable.jb-assignment.shakhtarov.me/` environment.
