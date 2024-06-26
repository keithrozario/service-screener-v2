import sysconfig

ROOT_DIR = str(sysconfig.get_paths()["purelib"]) + "/aws_service_screener"

SERVICE_DIR = ROOT_DIR + '/services'
TEMPLATE_DIR = ROOT_DIR + '/templates'
FRAMEWORK_DIR = ROOT_DIR + '/frameworks'
BOTOCORE_DIR = ROOT_DIR + '/../lib64/python3.7/site-packages/botocore'

HTML_FOLDER =  '/adminlte/aws/res'
ADMINLTE_ROOT_DIR = ROOT_DIR + '/adminlte'
ADMINLTE_DIR = ADMINLTE_ROOT_DIR + '/aws'
HTMLRES_DIR = ROOT_DIR + '/' + HTML_FOLDER
FORK_DIR = ROOT_DIR + '/__fork'
API_JSON = FORK_DIR + '/api.json'

GENERAL_CONF_PATH = SERVICE_DIR + '/general.reporter.json'

CLI_TRUE_KEYWORD_ARRAY = ['yes', 'y', 'true', '1', 1]

SESSUID_FILENAME = 'sess-uuid'