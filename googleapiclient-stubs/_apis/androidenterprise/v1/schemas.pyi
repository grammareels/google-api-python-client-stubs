import typing

import typing_extensions

@typing.type_check_only
class Administrator(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class AdministratorWebToken(typing_extensions.TypedDict, total=False):
    token: str

@typing.type_check_only
class AdministratorWebTokenSpec(typing_extensions.TypedDict, total=False):
    managedConfigurations: AdministratorWebTokenSpecManagedConfigurations
    parent: str
    permission: typing.List[str]
    playSearch: AdministratorWebTokenSpecPlaySearch
    privateApps: AdministratorWebTokenSpecPrivateApps
    storeBuilder: AdministratorWebTokenSpecStoreBuilder
    webApps: AdministratorWebTokenSpecWebApps

@typing.type_check_only
class AdministratorWebTokenSpecManagedConfigurations(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecPlaySearch(typing_extensions.TypedDict, total=False):
    approveApps: bool
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecPrivateApps(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecStoreBuilder(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdministratorWebTokenSpecWebApps(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AppRestrictionsSchema(typing_extensions.TypedDict, total=False):
    kind: str
    restrictions: typing.List[AppRestrictionsSchemaRestriction]

@typing.type_check_only
class AppRestrictionsSchemaChangeEvent(typing_extensions.TypedDict, total=False):
    productId: str

@typing.type_check_only
class AppRestrictionsSchemaRestriction(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class AppRestrictionsSchemaRestrictionRestrictionValue(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "bool",
        "string",
        "integer",
        "choice",
        "multiselect",
        "hidden",
        "bundle",
        "bundleArray",
    ]
    valueBool: bool
    valueInteger: int
    valueMultiselect: typing.List[str]
    valueString: str

@typing.type_check_only
class AppState(typing_extensions.TypedDict, total=False):
    keyedAppState: typing.List[KeyedAppState]
    packageName: str

@typing.type_check_only
class AppUpdateEvent(typing_extensions.TypedDict, total=False):
    productId: str

@typing.type_check_only
class AppVersion(typing_extensions.TypedDict, total=False):
    isProduction: bool
    track: typing_extensions.Literal[
        "appTrackUnspecified", "production", "beta", "alpha"
    ]
    trackId: typing.List[str]
    versionCode: int
    versionString: str

@typing.type_check_only
class ApprovalUrlInfo(typing_extensions.TypedDict, total=False):
    approvalUrl: str

@typing.type_check_only
class AuthenticationToken(typing_extensions.TypedDict, total=False):
    token: str

@typing.type_check_only
class AutoInstallConstraint(typing_extensions.TypedDict, total=False):
    chargingStateConstraint: typing_extensions.Literal[
        "chargingStateConstraintUnspecified", "chargingNotRequired", "chargingRequired"
    ]
    deviceIdleStateConstraint: typing_extensions.Literal[
        "deviceIdleStateConstraintUnspecified",
        "deviceIdleNotRequired",
        "deviceIdleRequired",
    ]
    networkTypeConstraint: typing_extensions.Literal[
        "networkTypeConstraintUnspecified", "anyNetwork", "unmeteredNetwork"
    ]

@typing.type_check_only
class AutoInstallPolicy(typing_extensions.TypedDict, total=False):
    autoInstallConstraint: typing.List[AutoInstallConstraint]
    autoInstallMode: typing_extensions.Literal[
        "autoInstallModeUnspecified",
        "doNotAutoInstall",
        "autoInstallOnce",
        "forceAutoInstall",
    ]
    autoInstallPriority: int
    minimumVersionCode: int

@typing.type_check_only
class ConfigurationVariables(typing_extensions.TypedDict, total=False):
    mcmId: str
    variableSet: typing.List[VariableSet]

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    androidId: str
    managementType: typing_extensions.Literal[
        "managedDevice", "managedProfile", "containerApp", "unmanagedProfile"
    ]
    policy: Policy
    report: DeviceReport

@typing.type_check_only
class DeviceReport(typing_extensions.TypedDict, total=False):
    appState: typing.List[AppState]
    lastUpdatedTimestampMillis: str

@typing.type_check_only
class DeviceReportUpdateEvent(typing_extensions.TypedDict, total=False):
    deviceId: str
    report: DeviceReport
    userId: str

@typing.type_check_only
class DeviceState(typing_extensions.TypedDict, total=False):
    accountState: typing_extensions.Literal["enabled", "disabled"]

@typing.type_check_only
class DevicesListResponse(typing_extensions.TypedDict, total=False):
    device: typing.List[Device]

@typing.type_check_only
class Enterprise(typing_extensions.TypedDict, total=False):
    administrator: typing.List[Administrator]
    id: str
    name: str
    primaryDomain: str

@typing.type_check_only
class EnterpriseAccount(typing_extensions.TypedDict, total=False):
    accountEmail: str

@typing.type_check_only
class EnterprisesListResponse(typing_extensions.TypedDict, total=False):
    enterprise: typing.List[Enterprise]

@typing.type_check_only
class EnterprisesSendTestPushNotificationResponse(
    typing_extensions.TypedDict, total=False
):
    messageId: str
    topicName: str

@typing.type_check_only
class Entitlement(typing_extensions.TypedDict, total=False):
    productId: str
    reason: typing_extensions.Literal["free", "groupLicense", "userPurchase"]

@typing.type_check_only
class EntitlementsListResponse(typing_extensions.TypedDict, total=False):
    entitlement: typing.List[Entitlement]

@typing.type_check_only
class GroupLicense(typing_extensions.TypedDict, total=False):
    acquisitionKind: typing_extensions.Literal["free", "bulkPurchase"]
    approval: typing_extensions.Literal["approved", "unapproved"]
    numProvisioned: int
    numPurchased: int
    permissions: typing_extensions.Literal[
        "currentApproved", "needsReapproval", "allCurrentAndFutureApproved"
    ]
    productId: str

@typing.type_check_only
class GroupLicenseUsersListResponse(typing_extensions.TypedDict, total=False):
    user: typing.List[User]

@typing.type_check_only
class GroupLicensesListResponse(typing_extensions.TypedDict, total=False):
    groupLicense: typing.List[GroupLicense]

@typing.type_check_only
class Install(typing_extensions.TypedDict, total=False):
    installState: typing_extensions.Literal["installed", "installPending"]
    productId: str
    versionCode: int

@typing.type_check_only
class InstallFailureEvent(typing_extensions.TypedDict, total=False):
    deviceId: str
    failureDetails: str
    failureReason: typing_extensions.Literal["unknown", "timeout"]
    productId: str
    userId: str

@typing.type_check_only
class InstallsListResponse(typing_extensions.TypedDict, total=False):
    install: typing.List[Install]

@typing.type_check_only
class KeyedAppState(typing_extensions.TypedDict, total=False):
    data: str
    key: str
    message: str
    severity: typing_extensions.Literal[
        "severityUnknown", "severityInfo", "severityError"
    ]
    stateTimestampMillis: str

@typing.type_check_only
class LocalizedText(typing_extensions.TypedDict, total=False):
    locale: str
    text: str

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    durationMs: str
    startTimeAfterMidnightMs: str

@typing.type_check_only
class ManagedConfiguration(typing_extensions.TypedDict, total=False):
    configurationVariables: ConfigurationVariables
    kind: str
    managedProperty: typing.List[ManagedProperty]
    productId: str

@typing.type_check_only
class ManagedConfigurationsForDeviceListResponse(
    typing_extensions.TypedDict, total=False
):
    managedConfigurationForDevice: typing.List[ManagedConfiguration]

@typing.type_check_only
class ManagedConfigurationsForUserListResponse(
    typing_extensions.TypedDict, total=False
):
    managedConfigurationForUser: typing.List[ManagedConfiguration]

@typing.type_check_only
class ManagedConfigurationsSettings(typing_extensions.TypedDict, total=False):
    lastUpdatedTimestampMillis: str
    mcmId: str
    name: str

@typing.type_check_only
class ManagedConfigurationsSettingsListResponse(
    typing_extensions.TypedDict, total=False
):
    managedConfigurationsSettings: typing.List[ManagedConfigurationsSettings]

@typing.type_check_only
class ManagedProperty(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ManagedPropertyBundle(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class NewDeviceEvent(typing_extensions.TypedDict, total=False):
    deviceId: str
    dpcPackageName: str
    managementType: typing_extensions.Literal["managedDevice", "managedProfile"]
    userId: str

@typing.type_check_only
class NewPermissionsEvent(typing_extensions.TypedDict, total=False):
    approvedPermissions: typing.List[str]
    productId: str
    requestedPermissions: typing.List[str]

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    appRestrictionsSchemaChangeEvent: AppRestrictionsSchemaChangeEvent
    appUpdateEvent: AppUpdateEvent
    deviceReportUpdateEvent: DeviceReportUpdateEvent
    enterpriseId: str
    installFailureEvent: InstallFailureEvent
    newDeviceEvent: NewDeviceEvent
    newPermissionsEvent: NewPermissionsEvent
    notificationType: typing_extensions.Literal[
        "unknown",
        "testNotification",
        "productApproval",
        "installFailure",
        "appUpdate",
        "newPermissions",
        "appRestricionsSchemaChange",
        "productAvailabilityChange",
        "newDevice",
        "deviceReportUpdate",
    ]
    productApprovalEvent: ProductApprovalEvent
    productAvailabilityChangeEvent: ProductAvailabilityChangeEvent
    timestampMillis: str

@typing.type_check_only
class NotificationSet(typing_extensions.TypedDict, total=False):
    notification: typing.List[Notification]
    notificationSetId: str

@typing.type_check_only
class PageInfo(typing_extensions.TypedDict, total=False):
    resultPerPage: int
    startIndex: int
    totalResults: int

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    permissionId: str

@typing.type_check_only
class Policy(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    appTracks: typing.List[TrackInfo]
    appVersion: typing.List[AppVersion]
    authorName: str
    availableCountries: typing.List[str]
    availableTracks: typing.List[str]
    category: str
    contentRating: typing_extensions.Literal[
        "ratingUnknown", "all", "preTeen", "teen", "mature"
    ]
    description: str
    detailsUrl: str
    distributionChannel: typing_extensions.Literal[
        "publicGoogleHosted", "privateGoogleHosted", "privateSelfHosted"
    ]
    features: typing.List[str]
    iconUrl: str
    lastUpdatedTimestampMillis: str
    minAndroidSdkVersion: int
    permissions: typing.List[ProductPermission]
    productId: str
    productPricing: typing_extensions.Literal[
        "unknown", "free", "freeWithInAppPurchase", "paid"
    ]
    recentChanges: str
    requiresContainerApp: bool
    screenshotUrls: typing.List[str]
    signingCertificate: ProductSigningCertificate
    smallIconUrl: str
    title: str
    workDetailsUrl: str

@typing.type_check_only
class ProductApprovalEvent(typing_extensions.TypedDict, total=False):
    approved: typing_extensions.Literal["unknown", "approved", "unapproved"]
    productId: str

@typing.type_check_only
class ProductAvailabilityChangeEvent(typing_extensions.TypedDict, total=False):
    availabilityStatus: typing_extensions.Literal[
        "unknown", "available", "removed", "unpublished"
    ]
    productId: str

@typing.type_check_only
class ProductPermission(typing_extensions.TypedDict, total=False):
    permissionId: str
    state: typing_extensions.Literal["required", "accepted"]

@typing.type_check_only
class ProductPermissions(typing_extensions.TypedDict, total=False):
    permission: typing.List[ProductPermission]
    productId: str

@typing.type_check_only
class ProductPolicy(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ProductSet(typing_extensions.TypedDict, total=False):
    productId: typing.List[str]
    productSetBehavior: typing_extensions.Literal[
        "unknown", "whitelist", "includeAll", "allApproved"
    ]
    productVisibility: typing.List[ProductVisibility]

@typing.type_check_only
class ProductSigningCertificate(typing_extensions.TypedDict, total=False):
    certificateHashSha1: str
    certificateHashSha256: str

@typing.type_check_only
class ProductVisibility(typing_extensions.TypedDict, total=False):
    productId: str
    trackIds: typing.List[str]
    tracks: typing.List[str]

@typing.type_check_only
class ProductsApproveRequest(typing_extensions.TypedDict, total=False):
    approvalUrlInfo: ApprovalUrlInfo
    approvedPermissions: typing_extensions.Literal[
        "currentPermissionsOnly", "allPermissions"
    ]

@typing.type_check_only
class ProductsGenerateApprovalUrlResponse(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class ProductsListResponse(typing_extensions.TypedDict, total=False):
    pageInfo: PageInfo
    product: typing.List[Product]
    tokenPagination: TokenPagination

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    key: ServiceAccountKey
    name: str

@typing.type_check_only
class ServiceAccountKey(typing_extensions.TypedDict, total=False):
    data: str
    id: str
    publicData: str
    type: typing_extensions.Literal["googleCredentials", "pkcs12"]

@typing.type_check_only
class ServiceAccountKeysListResponse(typing_extensions.TypedDict, total=False):
    serviceAccountKey: typing.List[ServiceAccountKey]

@typing.type_check_only
class SignupInfo(typing_extensions.TypedDict, total=False):
    completionToken: str
    kind: str
    url: str

@typing.type_check_only
class StoreCluster(typing_extensions.TypedDict, total=False):
    id: str
    name: typing.List[LocalizedText]
    orderInPage: str
    productId: typing.List[str]

@typing.type_check_only
class StoreLayout(typing_extensions.TypedDict, total=False):
    homepageId: str
    storeLayoutType: typing_extensions.Literal["unknown", "basic", "custom"]

@typing.type_check_only
class StoreLayoutClustersListResponse(typing_extensions.TypedDict, total=False):
    cluster: typing.List[StoreCluster]

@typing.type_check_only
class StoreLayoutPagesListResponse(typing_extensions.TypedDict, total=False):
    page: typing.List[StorePage]

@typing.type_check_only
class StorePage(typing_extensions.TypedDict, total=False):
    id: str
    link: typing.List[str]
    name: typing.List[LocalizedText]

@typing.type_check_only
class TokenPagination(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    previousPageToken: str

@typing.type_check_only
class TrackInfo(typing_extensions.TypedDict, total=False):
    trackAlias: str
    trackId: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    accountIdentifier: str
    accountType: typing_extensions.Literal["deviceAccount", "userAccount"]
    displayName: str
    id: str
    managementType: typing_extensions.Literal["googleManaged", "emmManaged"]
    primaryEmail: str

@typing.type_check_only
class UsersListResponse(typing_extensions.TypedDict, total=False):
    user: typing.List[User]

@typing.type_check_only
class VariableSet(typing_extensions.TypedDict, total=False):
    placeholder: str
    userValue: str

@typing.type_check_only
class WebApp(typing_extensions.TypedDict, total=False):
    displayMode: typing_extensions.Literal[
        "displayModeUnspecified", "minimalUi", "standalone", "fullScreen"
    ]
    icons: typing.List[WebAppIcon]
    isPublished: bool
    startUrl: str
    title: str
    versionCode: str
    webAppId: str

@typing.type_check_only
class WebAppIcon(typing_extensions.TypedDict, total=False):
    imageData: str

@typing.type_check_only
class WebAppsListResponse(typing_extensions.TypedDict, total=False):
    webApp: typing.List[WebApp]
