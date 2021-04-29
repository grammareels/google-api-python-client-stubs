import typing

import typing_extensions

@typing.type_check_only
class AndroidAppAsset(typing_extensions.TypedDict, total=False):
    certificate: CertificateInfo
    packageName: str

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    androidApp: AndroidAppAsset
    web: WebAsset

@typing.type_check_only
class CertificateInfo(typing_extensions.TypedDict, total=False):
    sha256Fingerprint: str

@typing.type_check_only
class CheckResponse(typing_extensions.TypedDict, total=False):
    debugString: str
    errorCode: typing.List[str]
    linked: bool
    maxAge: str

@typing.type_check_only
class ListResponse(typing_extensions.TypedDict, total=False):
    debugString: str
    errorCode: typing.List[str]
    maxAge: str
    statements: typing.List[Statement]

@typing.type_check_only
class Statement(typing_extensions.TypedDict, total=False):
    relation: str
    source: Asset
    target: Asset

@typing.type_check_only
class WebAsset(typing_extensions.TypedDict, total=False):
    site: str
