from pathlib import Path


# Version of this library. Generally the same as the SDK version.
VERSION = '100.13.10'

# The DAML SDK version to download artifacts from.
DAML_SDK_VERSION = VERSION


ROOT = Path(__file__).absolute().parent.parent

DAML_SDK_BASE_URL = 'https://digitalassetsdk.bintray.com/DigitalAssetSDK'
GOOGLE_APIS_BASE_URL = 'https://raw.githubusercontent.com/googleapis/googleapis/master'

DAML_LF_JAR = f'daml-lf-archive-{DAML_SDK_VERSION}.jar'
LEDGER_API_TGZ = f'ledger-api-protos-{DAML_SDK_VERSION}.tar.gz'
GOOGLE_RPC_STATUS_PROTO = 'google-rpc-status.proto'


fetch_urls = {
    DAML_LF_JAR: f'{DAML_SDK_BASE_URL}/com/digitalasset/daml-lf-archive/{DAML_SDK_VERSION}/daml-lf-archive-{DAML_SDK_VERSION}.jar',
    LEDGER_API_TGZ: f'{DAML_SDK_BASE_URL}/com/digitalasset/ledger-api-protos/{DAML_SDK_VERSION}/ledger-api-protos-{DAML_SDK_VERSION}.tar.gz',
    GOOGLE_RPC_STATUS_PROTO: f'{GOOGLE_APIS_BASE_URL}/google/rpc/status.proto',
}
