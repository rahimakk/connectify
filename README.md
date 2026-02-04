#  Connectify – Full Stack App + API Automation + CI/CD

##  Project Overview

**Connectify** is a full-stack user management system built to demonstrate:

- Backend API Development  
- Frontend Integration  
- API Automation using Postman  
- CI/CD Pipeline using GitHub Actions + Newman  

This project simulates how real-world applications are **built, tested automatically, and validated in a DevOps pipeline**.

---

##  Project Structure

```
connectify/
├── backend/                 # FastAPI backend (APIs + Database)
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── requirements.txt
├── frontend/                # HTML, CSS, JavaScript UI
│   ├── index.html
│   ├── style.css
│   └── script.js
├── postman/                 # Postman collection + environment
│   ├── Connectify.postman_collection.json
│   └── environment.json
├── .github/workflows/       # CI/CD pipeline
│   └── test.yml
└── README.md
```



---

##  Backend (FastAPI)

**Tech Used**
- FastAPI  
- SQLite  
- SQLAlchemy  
- Passlib (Password hashing)

###  Core API Features (CRUD)

| Operation | Method | Endpoint | Description |
|----------|--------|----------|-------------|
| Register | POST | `/register` | Create new user |
| Login | POST | `/login` | Authenticate user |
| Get All Users | GET | `/users` | Fetch all users |
| Get User by ID | GET | `/users/{id}` | Fetch single user |
| Update User | PATCH | `/users/{id}` | Update user details |
| Delete User | DELETE | `/users/{id}` | Remove user |
| Profile | GET | `/users/me` | Logged-in user info |

---

##  Frontend

Built using:
- HTML  
- CSS  
- JavaScript (Fetch API)

### UI Features
- User Registration  
- User Login  
- Dashboard  
- Search user by ID or Name  
- Update Profile  
- Logout  

Frontend communicates directly with backend APIs.

---

##  API Automation (Postman)

- Located inside `/postman`
- We implemented **end-to-end API automation**.

###  API Chaining Flow
- Register → Save Email
- Login → Save Token
- Get Users → Use Token
- Update User → Use ID
- Delete User → Validate Deletion

---


###  Scripts Used

**Pre-request Script (Dynamic Data)**

```js
const randomEmail = `user_${Date.now()}@test.com`;
pm.environment.set("email", randomEmail);
```

**Post Response test**
```js
pm.test("Status code check", () => {
    pm.expect(pm.response.code).to.be.oneOf([200,201]);
});
```

***What This Achieves***
1. Assertions
2. Dynamic data handling
3. Token storage
4. Automated validation



