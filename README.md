# dukaan_service

## Development

Build the image:

```bash
docker-compose build
```

Run the web server:

```bash
docker-compose up
```

Open your browser with URL `http://localhost:8080`.
For the admin panel `http://localhost:8080/admin`
(user: `1111`, password: `7879`).

Run the tests only once:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' dukaan_service
```

Run the tests and leave bash open inside the container, so it's possible to
re-run the tests faster again using `bash scripts/run-tests.sh [--keepdb]`:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh --bash-on-finish' dukaan_service
```

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' dukaan_service
```
# dukaan_service
