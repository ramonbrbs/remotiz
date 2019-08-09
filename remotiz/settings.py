ENV= 'DEV' # 'DEV' OR 'PROD'

if ENV == 'DEV':
    from .settings_dev import *
else:
    from .settings_prod import *
