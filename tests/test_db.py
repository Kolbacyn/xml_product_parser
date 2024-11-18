from conftest import BASE_DIR

try:
    from app.core.config import settings
except (NameError, ImportError) as error:
    raise AssertionError(
        'При импорте настроек приложения `Settings` из модуля '
        '`app.core.config` возникло исключение:\n'
        f'{type(error).__name__}: {error}.'
    )


def test_check_migration_file_exist():
    app_dirs = [d.name for d in BASE_DIR.iterdir()]
    assert 'migrations' in app_dirs, (
        'В корневой директории не обнаружена папка `migrations`.'
    )
    
    ALEMBIC_DIR = BASE_DIR / 'migrations'
    if not ALEMBIC_DIR.exists() or not ALEMBIC_DIR.is_dir():
        raise AssertionError('Папка `migrations` не существует или не является директорией.')
    
    version_dir = [d.name for d in ALEMBIC_DIR.iterdir()]
    assert 'versions' in version_dir, (
        'В папке `migrations` не обнаружена папка `versions`'
    )
    
    VERSIONS_DIR = ALEMBIC_DIR / 'versions'
    if not VERSIONS_DIR.exists() or not VERSIONS_DIR.is_dir():
        raise AssertionError('Папка `versions` не существует или не является директорией.')

    files_in_version_dir = [
        f.name for f in VERSIONS_DIR.iterdir()
        if f.is_file() and f.name != '__init__.py'
    ]
    assert len(files_in_version_dir) > 0, (
        'В папке `migrations/versions` не обнаружены файлы миграций'
    )
