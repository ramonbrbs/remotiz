ENV= 'DEV' # 'DEV' OR 'PROD'

if ENV == 'DEV':
    from .settings_test import *
else:
    from .settings_prod import *