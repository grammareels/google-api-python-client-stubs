import typing

import typing_extensions

@typing.type_check_only
class ClaimDeviceRequest(typing_extensions.TypedDict, total=False):
    customerId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]

@typing.type_check_only
class ClaimDeviceResponse(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceName: str

@typing.type_check_only
class ClaimDevicesRequest(typing_extensions.TypedDict, total=False):
    claims: typing.List[PartnerClaim]

@typing.type_check_only
class Company(typing_extensions.TypedDict, total=False):
    adminEmails: typing.List[str]
    companyId: str
    companyName: str
    name: str
    ownerEmails: typing.List[str]
    termsStatus: typing_extensions.Literal[
        "TERMS_STATUS_UNSPECIFIED",
        "TERMS_STATUS_NOT_ACCEPTED",
        "TERMS_STATUS_ACCEPTED",
        "TERMS_STATUS_STALE",
    ]

@typing.type_check_only
class Configuration(typing_extensions.TypedDict, total=False):
    companyName: str
    configurationId: str
    configurationName: str
    contactEmail: str
    contactPhone: str
    customMessage: str
    dpcExtras: str
    dpcResourcePath: str
    isDefault: bool
    name: str

@typing.type_check_only
class CreateCustomerRequest(typing_extensions.TypedDict, total=False):
    customer: Company

@typing.type_check_only
class CustomerApplyConfigurationRequest(typing_extensions.TypedDict, total=False):
    configuration: str
    device: DeviceReference

@typing.type_check_only
class CustomerListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    configurations: typing.List[Configuration]

@typing.type_check_only
class CustomerListCustomersResponse(typing_extensions.TypedDict, total=False):
    customers: typing.List[Company]
    nextPageToken: str

@typing.type_check_only
class CustomerListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str

@typing.type_check_only
class CustomerListDpcsResponse(typing_extensions.TypedDict, total=False):
    dpcs: typing.List[Dpc]

@typing.type_check_only
class CustomerRemoveConfigurationRequest(typing_extensions.TypedDict, total=False):
    device: DeviceReference

@typing.type_check_only
class CustomerUnclaimDeviceRequest(typing_extensions.TypedDict, total=False):
    device: DeviceReference

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    claims: typing.List[DeviceClaim]
    configuration: str
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
    name: str

@typing.type_check_only
class DeviceClaim(typing_extensions.TypedDict, total=False):
    ownerCompanyId: str
    resellerId: str
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeExpireTime: str
    vacationModeStartTime: str

@typing.type_check_only
class DeviceIdentifier(typing_extensions.TypedDict, total=False):
    imei: str
    manufacturer: str
    meid: str
    model: str
    serialNumber: str

@typing.type_check_only
class DeviceMetadata(typing_extensions.TypedDict, total=False):
    entries: typing.Dict[str, typing.Any]

@typing.type_check_only
class DeviceReference(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier

@typing.type_check_only
class DevicesLongRunningOperationMetadata(typing_extensions.TypedDict, total=False):
    devicesCount: int
    processingStatus: typing_extensions.Literal[
        "BATCH_PROCESS_STATUS_UNSPECIFIED",
        "BATCH_PROCESS_PENDING",
        "BATCH_PROCESS_IN_PROGRESS",
        "BATCH_PROCESS_PROCESSED",
    ]
    progress: int

@typing.type_check_only
class DevicesLongRunningOperationResponse(typing_extensions.TypedDict, total=False):
    perDeviceStatus: typing.List[OperationPerDevice]
    successCount: int

@typing.type_check_only
class Dpc(typing_extensions.TypedDict, total=False):
    dpcName: str
    name: str
    packageName: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FindDevicesByDeviceIdentifierRequest(typing_extensions.TypedDict, total=False):
    deviceIdentifier: DeviceIdentifier
    limit: str
    pageToken: str

@typing.type_check_only
class FindDevicesByDeviceIdentifierResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class FindDevicesByOwnerRequest(typing_extensions.TypedDict, total=False):
    customerId: typing.List[str]
    limit: str
    pageToken: str
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]

@typing.type_check_only
class FindDevicesByOwnerResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListCustomersResponse(typing_extensions.TypedDict, total=False):
    customers: typing.List[Company]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListVendorCustomersResponse(typing_extensions.TypedDict, total=False):
    customers: typing.List[Company]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListVendorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    vendors: typing.List[Company]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationPerDevice(typing_extensions.TypedDict, total=False):
    claim: PartnerClaim
    result: PerDeviceStatusInBatch
    unclaim: PartnerUnclaim
    updateMetadata: UpdateMetadataArguments

@typing.type_check_only
class PartnerClaim(typing_extensions.TypedDict, total=False):
    customerId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]

@typing.type_check_only
class PartnerUnclaim(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeDays: int
    vacationModeExpireTime: str

@typing.type_check_only
class PerDeviceStatusInBatch(typing_extensions.TypedDict, total=False):
    deviceId: str
    errorIdentifier: str
    errorMessage: str
    status: typing_extensions.Literal[
        "SINGLE_DEVICE_STATUS_UNSPECIFIED",
        "SINGLE_DEVICE_STATUS_UNKNOWN_ERROR",
        "SINGLE_DEVICE_STATUS_OTHER_ERROR",
        "SINGLE_DEVICE_STATUS_SUCCESS",
        "SINGLE_DEVICE_STATUS_PERMISSION_DENIED",
        "SINGLE_DEVICE_STATUS_INVALID_DEVICE_IDENTIFIER",
        "SINGLE_DEVICE_STATUS_INVALID_SECTION_TYPE",
        "SINGLE_DEVICE_STATUS_SECTION_NOT_YOURS",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UnclaimDeviceRequest(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeDays: int
    vacationModeExpireTime: str

@typing.type_check_only
class UnclaimDevicesRequest(typing_extensions.TypedDict, total=False):
    unclaims: typing.List[PartnerUnclaim]

@typing.type_check_only
class UpdateDeviceMetadataInBatchRequest(typing_extensions.TypedDict, total=False):
    updates: typing.List[UpdateMetadataArguments]

@typing.type_check_only
class UpdateDeviceMetadataRequest(typing_extensions.TypedDict, total=False):
    deviceMetadata: DeviceMetadata

@typing.type_check_only
class UpdateMetadataArguments(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
