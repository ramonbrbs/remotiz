ENV= 'DEV' # 'DEV' OR 'PROD'

if ENV == 'PROD':
    from .settings_test import *
else:
    from .settings_prod import *
