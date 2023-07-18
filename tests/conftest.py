import pytest
from alembic.command import upgrade
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient
from app.main import app
from app.core.models import Base


@pytest.fixture(scope='function')
def test_app(test_db):
    # todo: решить вопрос с тестовой бд
    app.dependency_overrides[get_session] = lambda: test_db
    client = TestClient(app)
    yield client


@pytest.fixture(scope='function')
def test_db():
    # Создание новой базы данных для тестирования
    engine = create_engine(
        url='',
        echo=False
    )

    # Применение миграций Alembic
    alembic_cfg = Config('alembic.ini')
    upgrade(alembic_cfg, 'head')

    Base.metadata.create_all(bind=engine)

    def get_session():
        with Session(engine, autoflush=False) as session:
            yield session

    yield from get_session()  # Тесты выполняются здесь

    # После выполнения тестов база данных удаляется
    Base.metadata.drop_all(bind=engine)
