# Django settings for mediamachine project.
import os.path
from ccnmtlsettings.shared import common

project = 'mediamachine'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'mediamachine.machine',
]

INSTALLED_APPS += [  # noqa
    'mediamachine.machine',
    'django_databrowse',
]
