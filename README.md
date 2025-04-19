# 🚀 KraftBase

KraftBase is a full-stack project that combines a modern frontend with a FastAPI backend and RabbitMQ message broker for real-time device management and communication.

---

## 🧰 Tech Stack

- **Frontend**: React (served on port `3000`)
- **Backend**: FastAPI (served on port `8000`)
- **Messaging**: RabbitMQ (default management port `15672`)
- **Containerization**: Docker & Docker Compose

---

## 📁 Project Structure

```
KraftBase-main/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   └── ...
│   └── Dockerfile
├── frontend/
│   └── (React app files)
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🏗️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/KraftBase.git
cd KraftBase
```

### 2. Start the application

```bash
docker-compose up --build
```

This will start:
- 🖥️ Frontend on [http://localhost:3000](http://localhost:3000)
- ⚙️ Backend on [http://localhost:8000](http://localhost:8000)
- 📬 RabbitMQ dashboard on [http://localhost:15672](http://localhost:15672)

> RabbitMQ default credentials:
> - **User**: `guest`
> - **Password**: `guest`

---

## 📡 API Endpoints

Here are some example endpoints from the FastAPI backend:

- `POST /devices/register` - Register a new device
- `GET /devices` - List all devices
- `POST /publish` - Publish message to RabbitMQ

Swagger Docs are available at:  
📚 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Commands

- Start containers: `docker-compose up --build`
- Stop containers: `docker-compose down`
- Check running containers: `docker ps`

---

## 🧪 Development Tips

- The backend uses `--reload` for auto-reloading on changes.
- If you make code changes, simply restart the backend container:
  
```bash
docker-compose restart backend
```

- Access RabbitMQ web UI at [localhost:15672](http://localhost:15672)

---

## 🛠️ Troubleshooting

- **Backend crashing with `ModuleNotFoundError`**?  
  Check your `command:` in `docker-compose.yml`. Use:

  ```yaml
  command: uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
  ```

- **Frontend loads but backend errors?**  
  Make sure the backend is running on port `8000`, and your frontend is pointing to the correct API base URL.

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/cool-feature`)
3. Commit your changes (`git commit -m 'Add cool feature'`)
4. Push to the branch (`git push origin feature/cool-feature`)
5. Open a pull request

---

## 📜 License

MIT License. Feel free to use, share, and improve!

---

## 📬 Contact

Got questions or feedback? Reach out via [GitHub Issues](https://github.com/yourusername/KraftBase/issues)
