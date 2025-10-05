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

| Environment |                           URL                           |
|:-----------:|:-------------------------------------------------------:|
|     DEV     | https://{YOUR_BRANCH_NAME}.jb-assignment.shakhtarov.me/ |
|    STAGE    |        https://stage.jb-assignment.shakhtarov.me/       |
|     PROD    |           https://jb-assignment.shakhtarov.me/          |

### Deploy to dev

In order to create a dedicated dev-environment you can simply checkout to you own branch and push the changes back to the corresponding branch of this repo.
It will create a new env for you with a following name: `https://{YOUR_BRANCH_NAME}.jb-assignment.shakhtarov.me`

> [!WARNING]
> Please do not use an underscore in a branch name since it is not a valid URL-symbol. It will probably fail your deploy job.

> [!IMPORTANT]
> Each development environment remains active as long as there has been activity in its corresponding branch within the last seven days. If no activity is detected during that period, the environment is automatically removed.

### Deploy to stage

After changes are stabilized, they are merged or rebased into the `stage` branch via a PR. This automatically triggers a pipeline to build, deploy and test a code on the `https://stage.jb-assignment.shakhtarov.me/` environment.

### Deploy to prod

After the `stage` environment passes all the tests, a manually approved production deployment is triggered. The previously stored commit SHA from a successful `stage` build is used to re-tag the existing image and deploy it to production. After a successful rollout, a pull request is created for a manual merge approval.