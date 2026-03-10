# B64 Translator

A web application for encoding and decoding Base64 strings, served with **Nginx** as reverse proxy and **Flask** as the backend API — all containerized with **Docker**.

---

## Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Frontend   | HTML / CSS / JS     |
| Backend    | Python + Flask      |
| Web Server | Nginx (Docker image)|
| Container  | Docker + Compose    |

---

## Project Structure

```
b64-translator/
├── docker-compose.yml
├── nginx/
│   └── nginx.conf
└── app/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    └── static/
        └── index.html
```

---

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## How to Run

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/b64-translator.git
cd b64-translator

# 2. Build and start all services
docker-compose up --build

# 3. Open browser
http://localhost:8080
```

To stop the app:
```bash
docker-compose down
```

---

## How to Use

### Via Web UI

1. Open `http://localhost:8080` in your browser
2. Click **[ ENCODE ]** to encode plain text → Base64
3. Click **[ DECODE ]** to decode Base64 → plain text
4. Type or paste your input in the left panel
5. Click the **→** button (or press `Ctrl+Enter`)
6. Result appears in the right panel
7. Click **COPY** to copy the result to clipboard

### Via API (cURL)

**Encode:**
```bash
curl -X POST http://localhost:8080/api/encode \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World"}'
```
Response:
```json
{"success": true, "result": "SGVsbG8gV29ybGQ="}
```

**Decode:**
```bash
curl -X POST http://localhost:8080/api/decode \
  -H "Content-Type: application/json" \
  -d '{"text": "SGVsbG8gV29ybGQ="}'
```
Response:
```json
{"success": true, "result": "Hello World"}
```

**Health Check:**
```bash
curl http://localhost:8080/api/health
```

---

## License

MIT
