from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='trust',
        display_name="Just Trust Game",
        num_demo_participants=2,
        app_sequence=['trust']
    ),
    dict(
        name='q',
        display_name="Just Q",
        num_demo_participants=1,
        app_sequence=['q']
    ),
    dict(
        name='full',
        display_name="Q and Trust together",
        num_demo_participants=2,
        app_sequence=['q', 'trust'],
        party_treatment=True,
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ 
<div class='bg-dark p-3'>
<a href='https://compsocialscience.github.io/summer-institute/2020/maastricht/' target='_blank'> 
<img src='https://compsocialscience.github.io/summer-institute/assets/images/sicss-logo.svg' >
</a>

</div>
<div class='my-3 '><a href='https://github.com/chapkovski/sicss-maastricht' target='_blank'>Click here for the code</a></div>
"""

SECRET_KEY = 'cy=-*y3foj=t7twrak$yqu@)75+&=lof2tg!q#3uvvv3dy-ll4'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
