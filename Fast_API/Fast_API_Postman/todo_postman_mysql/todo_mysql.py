# ============================================================
# 🔐 FastAPI TODO App + MySQL + JWT Authentication
# ============================================================

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MYSQL CONFIGURATION
# ============================================================

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/todo_db"

# ------------------------------------------------------------


engine = create_engine(DATABASE_URL)

# ------------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ------------------------------------------------------------

Base = declarative_base()

# ============================================================
# 🗃️ DATABASE MODEL
# ============================================================


class TodoTable(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    completed = Column(Boolean, default=False)

# ============================================================
# 🏗️ CREATE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🔄 DATABASE DEPENDENCY
# ============================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE = timedelta(minutes=10)

# ============================================================
# 🧾 Pydantic Models
# ============================================================

class Todo(BaseModel):

    id: int
    title: str
    completed: bool = False

# ------------------------------------------------------------

class Login(BaseModel):

    username: str
    password: str

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ------------------------------------------------------------

def verify_token(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI + MySQL + JWT CRUD 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):

    '''
    Dummy Login

    Username = admin
    Password = admin123
    '''

    if user.username != "admin" or user.password != "admin123":

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "10 minutes"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(
    todo: Todo,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    '''
    Check duplicate ID
    '''

    existing_todo = db.query(TodoTable).filter(
        TodoTable.id == todo.id
    ).first()

    if existing_todo:

        raise HTTPException(
            status_code=400,
            detail="ID already exists"
        )

    '''
    Create new todo object
    '''

    new_todo = TodoTable(
        id=todo.id,
        title=todo.title,
        completed=todo.completed
    )

    '''
    Save into MySQL
    '''

    db.add(new_todo)

    db.commit()

    db.refresh(new_todo)

    return {
        "message": "Todo created successfully",
        "data": new_todo
    }

# ============================================================
# ✅ READ ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos(
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todos = db.query(TodoTable).all()

    return {
        "count": len(todos),
        "data": todos
    }

# ============================================================
# ✅ READ SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoTable).filter(
        TodoTable.id == todo_id
    ).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo

# ============================================================
# ✅ UPDATE TODO
# ============================================================

@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    updated: Todo,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoTable).filter(
        TodoTable.id == todo_id
    ).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    '''
    Update fields
    '''

    todo.title = updated.title

    todo.completed = updated.completed

    db.commit()

    db.refresh(todo)

    return {
        "message": "Todo updated successfully",
        "data": todo
    }

# ============================================================
# ✅ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoTable).filter(
        TodoTable.id == todo_id
    ).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)

    db.commit()

    return {
        "message": "Todo deleted successfully"
    }
