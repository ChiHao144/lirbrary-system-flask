from sqlalchemy.sql.functions import now

from app import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from enum import Enum as RoleEnum, Enum


class UserRole(RoleEnum):
    ADMIN = 1
    STAFF = 2
    STUDENT = 3


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    full_name = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=False)
    user_role = Column(Enum(UserRole))

    def __str__(self):
        return self.full_name

    def get_role(self):
        return self.user_role


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=True)

    def __str__(self):
        return self.name


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    description = Column(String(255), nullable=False)


class Author(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __str__(self):
        return self.name


class BorrowingSlip(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey(User.id))
    created_date = Column(DateTime, default=now())
    is_return = Column(Boolean, nullable=True, default=False)


class BorrowingSlipDetail(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_borrowing_slip = Column(Integer, ForeignKey(BorrowingSlip.id))
    id_book = Column(Integer, ForeignKey(Book.id))


class Receipt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey(User), nullable=False)
    date = Column(DateTime, nullable=False, default=now())


class ReceiptDetail(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_book = Column(Integer, ForeignKey(Book.id))
    quantity = Column(Integer, nullable=False, default=1)


class Rule(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    value = Column(Integer, nullable=False)
