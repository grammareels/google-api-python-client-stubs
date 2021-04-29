import typing

import typing_extensions

@typing.type_check_only
class BatchDeleteJobsRequest(typing_extensions.TypedDict, total=False):
    filter: str

AlternativeBucketRange = typing_extensions.TypedDict(
    "AlternativeBucketRange",
    {
        "from": float,
        "to": float,
    },
    total=False,
)

@typing.type_check_only
class BucketRange(AlternativeBucketRange): ...

@typing.type_check_only
class BucketizedCount(typing_extensions.TypedDict, total=False):
    count: int
    range: BucketRange

@typing.type_check_only
class CommuteInfo(typing_extensions.TypedDict, total=False):
    jobLocation: JobLocation
    travelDuration: str

@typing.type_check_only
class CommutePreference(typing_extensions.TypedDict, total=False):
    allowNonStreetLevelAddress: bool
    departureHourLocal: int
    method: typing_extensions.Literal[
        "COMMUTE_METHOD_UNSPECIFIED", "DRIVING", "TRANSIT"
    ]
    roadTraffic: typing_extensions.Literal[
        "ROAD_TRAFFIC_UNSPECIFIED", "TRAFFIC_FREE", "BUSY_HOUR"
    ]
    startLocation: LatLng
    travelTime: str

@typing.type_check_only
class Company(typing_extensions.TypedDict, total=False):
    careerPageLink: str
    companyInfoSources: typing.List[CompanyInfoSource]
    companySize: typing_extensions.Literal[
        "COMPANY_SIZE_UNSPECIFIED",
        "MINI",
        "SMALL",
        "SMEDIUM",
        "MEDIUM",
        "BIG",
        "BIGGER",
        "GIANT",
    ]
    disableLocationOptimization: bool
    displayName: str
    distributorBillingCompanyId: str
    distributorCompanyId: str
    eeoText: str
    hiringAgency: bool
    hqLocation: str
    imageUrl: str
    keywordSearchableCustomAttributes: typing.List[str]
    keywordSearchableCustomFields: typing.List[int]
    name: str
    structuredCompanyHqLocation: JobLocation
    suspended: bool
    title: str
    website: str

@typing.type_check_only
class CompanyInfoSource(typing_extensions.TypedDict, total=False):
    freebaseMid: str
    gplusId: str
    mapsCid: str
    unknownTypeId: str

@typing.type_check_only
class CompensationEntry(typing_extensions.TypedDict, total=False):
    amount: Money
    description: str
    expectedUnitsPerYear: float
    range: CompensationRange
    type: typing_extensions.Literal[
        "COMPENSATION_TYPE_UNSPECIFIED",
        "BASE",
        "BONUS",
        "SIGNING_BONUS",
        "EQUITY",
        "PROFIT_SHARING",
        "COMMISSIONS",
        "TIPS",
        "OTHER_COMPENSATION_TYPE",
    ]
    unit: typing_extensions.Literal[
        "COMPENSATION_UNIT_UNSPECIFIED",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
        "ONE_TIME",
        "OTHER_COMPENSATION_UNIT",
    ]

@typing.type_check_only
class CompensationFilter(typing_extensions.TypedDict, total=False):
    includeJobsWithUnspecifiedCompensationRange: bool
    range: CompensationRange
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]
    units: typing.List[str]

@typing.type_check_only
class CompensationHistogramRequest(typing_extensions.TypedDict, total=False):
    bucketingOption: NumericBucketingOption
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

@typing.type_check_only
class CompensationHistogramResult(typing_extensions.TypedDict, total=False):
    result: NumericBucketingResult
    type: typing_extensions.Literal[
        "COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED",
        "BASE",
        "ANNUALIZED_BASE",
        "ANNUALIZED_TOTAL",
    ]

@typing.type_check_only
class CompensationInfo(typing_extensions.TypedDict, total=False):
    amount: Money
    annualizedBaseCompensationRange: CompensationRange
    annualizedTotalCompensationRange: CompensationRange
    entries: typing.List[CompensationEntry]
    max: Money
    min: Money
    type: typing_extensions.Literal[
        "JOB_COMPENSATION_TYPE_UNSPECIFIED",
        "HOURLY",
        "SALARY",
        "PER_PROJECT",
        "COMMISSION",
        "OTHER_TYPE",
    ]

@typing.type_check_only
class CompensationRange(typing_extensions.TypedDict, total=False):
    max: Money
    min: Money

@typing.type_check_only
class CompleteQueryResponse(typing_extensions.TypedDict, total=False):
    completionResults: typing.List[CompletionResult]
    metadata: ResponseMetadata

@typing.type_check_only
class CompletionResult(typing_extensions.TypedDict, total=False):
    imageUrl: str
    suggestion: str
    type: typing_extensions.Literal[
        "COMPLETION_TYPE_UNSPECIFIED", "JOB_TITLE", "COMPANY_NAME", "COMBINED"
    ]

@typing.type_check_only
class CreateJobRequest(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    job: Job
    processingOptions: JobProcessingOptions

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    filterable: bool
    longValue: str
    stringValues: StringValues

@typing.type_check_only
class CustomAttributeHistogramRequest(typing_extensions.TypedDict, total=False):
    key: str
    longValueHistogramBucketingOption: NumericBucketingOption
    stringValueHistogram: bool

@typing.type_check_only
class CustomAttributeHistogramResult(typing_extensions.TypedDict, total=False):
    key: str
    longValueHistogramResult: NumericBucketingResult
    stringValueHistogramResult: typing.Dict[str, typing.Any]

@typing.type_check_only
class CustomField(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

@typing.type_check_only
class CustomFieldFilter(typing_extensions.TypedDict, total=False):
    queries: typing.List[str]
    type: typing_extensions.Literal["FILTER_TYPE_UNSPECIFIED", "OR", "AND", "NOT"]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeleteJobsByFilterRequest(typing_extensions.TypedDict, total=False):
    disableFastProcess: bool
    filter: Filter

@typing.type_check_only
class DeviceInfo(typing_extensions.TypedDict, total=False):
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "WEB", "MOBILE_WEB", "ANDROID", "IOS", "BOT", "OTHER"
    ]
    id: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExtendedCompensationFilter(typing_extensions.TypedDict, total=False):
    compensationRange: ExtendedCompensationInfoCompensationRange
    compensationUnits: typing.List[str]
    currency: str
    includeJobWithUnspecifiedCompensationRange: bool
    type: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "UNIT_ONLY",
        "UNIT_AND_AMOUNT",
        "ANNUALIZED_BASE_AMOUNT",
        "ANNUALIZED_TOTAL_AMOUNT",
    ]

@typing.type_check_only
class ExtendedCompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: ExtendedCompensationInfoCompensationRange
    annualizedBaseCompensationUnspecified: bool
    annualizedTotalCompensationRange: ExtendedCompensationInfoCompensationRange
    annualizedTotalCompensationUnspecified: bool
    currency: str
    entries: typing.List[ExtendedCompensationInfoCompensationEntry]

@typing.type_check_only
class ExtendedCompensationInfoCompensationEntry(
    typing_extensions.TypedDict, total=False
):
    amount: ExtendedCompensationInfoDecimal
    description: str
    expectedUnitsPerYear: ExtendedCompensationInfoDecimal
    range: ExtendedCompensationInfoCompensationRange
    type: typing_extensions.Literal[
        "EXTENDED_COMPENSATION_TYPE_UNSPECIFIED",
        "BASE",
        "BONUS",
        "SIGNING_BONUS",
        "EQUITY",
        "PROFIT_SHARING",
        "COMMISSIONS",
        "TIPS",
        "OTHER_COMPENSATION_TYPE",
    ]
    unit: typing_extensions.Literal[
        "EXTENDED_COMPENSATION_UNIT_UNSPECIFIED",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
        "ONE_TIME",
        "OTHER_COMPENSATION_UNIT",
    ]
    unspecified: bool

@typing.type_check_only
class ExtendedCompensationInfoCompensationRange(
    typing_extensions.TypedDict, total=False
):
    max: ExtendedCompensationInfoDecimal
    min: ExtendedCompensationInfoDecimal

@typing.type_check_only
class ExtendedCompensationInfoDecimal(typing_extensions.TypedDict, total=False):
    micros: int
    units: str

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    requisitionId: str

@typing.type_check_only
class GetHistogramRequest(typing_extensions.TypedDict, total=False):
    allowBroadening: bool
    filters: JobFilters
    query: JobQuery
    requestMetadata: RequestMetadata
    searchTypes: typing.List[str]

@typing.type_check_only
class GetHistogramResponse(typing_extensions.TypedDict, total=False):
    metadata: ResponseMetadata
    results: typing.List[HistogramResult]

@typing.type_check_only
class GoogleCloudTalentV4BatchCreateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

@typing.type_check_only
class GoogleCloudTalentV4BatchDeleteJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

@typing.type_check_only
class GoogleCloudTalentV4BatchOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    failureCount: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    stateDescription: str
    successCount: int
    totalCount: int
    updateTime: str

@typing.type_check_only
class GoogleCloudTalentV4BatchUpdateJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobResults: typing.List[GoogleCloudTalentV4JobResult]

@typing.type_check_only
class GoogleCloudTalentV4CompensationInfo(typing_extensions.TypedDict, total=False):
    annualizedBaseCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange
    annualizedTotalCompensationRange: GoogleCloudTalentV4CompensationInfoCompensationRange
    entries: typing.List[GoogleCloudTalentV4CompensationInfoCompensationEntry]

@typing.type_check_only
class GoogleCloudTalentV4CompensationInfoCompensationEntry(
    typing_extensions.TypedDict, total=False
):
    amount: Money
    description: str
    expectedUnitsPerYear: float
    range: GoogleCloudTalentV4CompensationInfoCompensationRange
    type: typing_extensions.Literal[
        "COMPENSATION_TYPE_UNSPECIFIED",
        "BASE",
        "BONUS",
        "SIGNING_BONUS",
        "EQUITY",
        "PROFIT_SHARING",
        "COMMISSIONS",
        "TIPS",
        "OTHER_COMPENSATION_TYPE",
    ]
    unit: typing_extensions.Literal[
        "COMPENSATION_UNIT_UNSPECIFIED",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
        "ONE_TIME",
        "OTHER_COMPENSATION_UNIT",
    ]

@typing.type_check_only
class GoogleCloudTalentV4CompensationInfoCompensationRange(
    typing_extensions.TypedDict, total=False
):
    maxCompensation: Money
    minCompensation: Money

@typing.type_check_only
class GoogleCloudTalentV4CustomAttribute(typing_extensions.TypedDict, total=False):
    filterable: bool
    keywordSearchable: bool
    longValues: typing.List[str]
    stringValues: typing.List[str]

@typing.type_check_only
class GoogleCloudTalentV4Job(typing_extensions.TypedDict, total=False):
    addresses: typing.List[str]
    applicationInfo: GoogleCloudTalentV4JobApplicationInfo
    company: str
    companyDisplayName: str
    compensationInfo: GoogleCloudTalentV4CompensationInfo
    customAttributes: typing.Dict[str, typing.Any]
    degreeTypes: typing.List[str]
    department: str
    derivedInfo: GoogleCloudTalentV4JobDerivedInfo
    description: str
    employmentTypes: typing.List[str]
    incentives: str
    jobBenefits: typing.List[str]
    jobEndTime: str
    jobLevel: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    jobStartTime: str
    languageCode: str
    name: str
    postingCreateTime: str
    postingExpireTime: str
    postingPublishTime: str
    postingRegion: typing_extensions.Literal[
        "POSTING_REGION_UNSPECIFIED", "ADMINISTRATIVE_AREA", "NATION", "TELECOMMUTE"
    ]
    postingUpdateTime: str
    processingOptions: GoogleCloudTalentV4JobProcessingOptions
    promotionValue: int
    qualifications: str
    requisitionId: str
    responsibilities: str
    title: str
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED",
        "ACCOUNT_ONLY",
        "SHARED_WITH_GOOGLE",
        "SHARED_WITH_PUBLIC",
    ]

@typing.type_check_only
class GoogleCloudTalentV4JobApplicationInfo(typing_extensions.TypedDict, total=False):
    emails: typing.List[str]
    instruction: str
    uris: typing.List[str]

@typing.type_check_only
class GoogleCloudTalentV4JobDerivedInfo(typing_extensions.TypedDict, total=False):
    jobCategories: typing.List[str]
    locations: typing.List[GoogleCloudTalentV4Location]

@typing.type_check_only
class GoogleCloudTalentV4JobProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

@typing.type_check_only
class GoogleCloudTalentV4JobResult(typing_extensions.TypedDict, total=False):
    job: GoogleCloudTalentV4Job
    status: Status

@typing.type_check_only
class GoogleCloudTalentV4Location(typing_extensions.TypedDict, total=False):
    latLng: LatLng
    locationType: typing_extensions.Literal[
        "LOCATION_TYPE_UNSPECIFIED",
        "COUNTRY",
        "ADMINISTRATIVE_AREA",
        "SUB_ADMINISTRATIVE_AREA",
        "LOCALITY",
        "POSTAL_CODE",
        "SUB_LOCALITY",
        "SUB_LOCALITY_1",
        "SUB_LOCALITY_2",
        "NEIGHBORHOOD",
        "STREET_ADDRESS",
    ]
    postalAddress: PostalAddress
    radiusMiles: float

@typing.type_check_only
class HistogramFacets(typing_extensions.TypedDict, total=False):
    compensationHistogramFacets: typing.List[CompensationHistogramRequest]
    customAttributeHistogramFacets: typing.List[CustomAttributeHistogramRequest]
    simpleHistogramFacets: typing.List[str]

@typing.type_check_only
class HistogramResult(typing_extensions.TypedDict, total=False):
    searchType: typing_extensions.Literal[
        "JOB_FIELD_UNSPECIFIED",
        "COMPANY_ID",
        "EMPLOYMENT_TYPE",
        "COMPANY_SIZE",
        "DATE_PUBLISHED",
        "CUSTOM_FIELD_1",
        "CUSTOM_FIELD_2",
        "CUSTOM_FIELD_3",
        "CUSTOM_FIELD_4",
        "CUSTOM_FIELD_5",
        "CUSTOM_FIELD_6",
        "CUSTOM_FIELD_7",
        "CUSTOM_FIELD_8",
        "CUSTOM_FIELD_9",
        "CUSTOM_FIELD_10",
        "CUSTOM_FIELD_11",
        "CUSTOM_FIELD_12",
        "CUSTOM_FIELD_13",
        "CUSTOM_FIELD_14",
        "CUSTOM_FIELD_15",
        "CUSTOM_FIELD_16",
        "CUSTOM_FIELD_17",
        "CUSTOM_FIELD_18",
        "CUSTOM_FIELD_19",
        "CUSTOM_FIELD_20",
        "EDUCATION_LEVEL",
        "EXPERIENCE_LEVEL",
        "ADMIN1",
        "COUNTRY",
        "CITY",
        "LOCALE",
        "LANGUAGE",
        "CATEGORY",
        "CITY_COORDINATE",
        "ADMIN1_COUNTRY",
        "COMPANY_TITLE",
        "COMPANY_DISPLAY_NAME",
        "BASE_COMPENSATION_UNIT",
    ]
    values: typing.Dict[str, typing.Any]

@typing.type_check_only
class HistogramResults(typing_extensions.TypedDict, total=False):
    compensationHistogramResults: typing.List[CompensationHistogramResult]
    customAttributeHistogramResults: typing.List[CustomAttributeHistogramResult]
    simpleHistogramResults: typing.List[HistogramResult]

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    applicationEmailList: typing.List[str]
    applicationInstruction: str
    applicationUrls: typing.List[str]
    benefits: typing.List[str]
    companyDisplayName: str
    companyName: str
    companyTitle: str
    compensationInfo: CompensationInfo
    createTime: str
    customAttributes: typing.Dict[str, typing.Any]
    department: str
    description: str
    distributorCompanyId: str
    educationLevels: typing.List[str]
    employmentTypes: typing.List[str]
    endDate: Date
    expireTime: str
    expiryDate: Date
    extendedCompensationInfo: ExtendedCompensationInfo
    filterableCustomFields: typing.Dict[str, typing.Any]
    incentives: str
    jobLocations: typing.List[JobLocation]
    jobTitle: str
    languageCode: str
    level: typing_extensions.Literal[
        "JOB_LEVEL_UNSPECIFIED",
        "ENTRY_LEVEL",
        "EXPERIENCED",
        "MANAGER",
        "DIRECTOR",
        "EXECUTIVE",
    ]
    locations: typing.List[str]
    name: str
    promotionValue: int
    publishDate: Date
    qualifications: str
    referenceUrl: str
    region: typing_extensions.Literal[
        "REGION_UNSPECIFIED", "STATE_WIDE", "NATION_WIDE", "TELECOMMUTE"
    ]
    requisitionId: str
    responsibilities: str
    startDate: Date
    unindexedCustomFields: typing.Dict[str, typing.Any]
    updateTime: str
    visibility: typing_extensions.Literal[
        "JOB_VISIBILITY_UNSPECIFIED", "PRIVATE", "GOOGLE", "PUBLIC"
    ]

@typing.type_check_only
class JobFilters(typing_extensions.TypedDict, total=False):
    categories: typing.List[str]
    commuteFilter: CommutePreference
    companyNames: typing.List[str]
    companyTitles: typing.List[str]
    compensationFilter: CompensationFilter
    customAttributeFilter: str
    customFieldFilters: typing.Dict[str, typing.Any]
    disableSpellCheck: bool
    employmentTypes: typing.List[str]
    extendedCompensationFilter: ExtendedCompensationFilter
    languageCodes: typing.List[str]
    locationFilters: typing.List[LocationFilter]
    publishDateRange: typing_extensions.Literal[
        "DATE_RANGE_UNSPECIFIED",
        "PAST_24_HOURS",
        "PAST_WEEK",
        "PAST_MONTH",
        "PAST_YEAR",
        "PAST_3_DAYS",
    ]
    query: str
    tenantJobOnly: bool

@typing.type_check_only
class JobLocation(typing_extensions.TypedDict, total=False):
    latLng: LatLng
    locationType: typing_extensions.Literal[
        "LOCATION_TYPE_UNSPECIFIED",
        "COUNTRY",
        "ADMINISTRATIVE_AREA",
        "SUB_ADMINISTRATIVE_AREA",
        "LOCALITY",
        "POSTAL_CODE",
        "SUB_LOCALITY",
        "SUB_LOCALITY_1",
        "SUB_LOCALITY_2",
        "NEIGHBORHOOD",
        "STREET_ADDRESS",
    ]
    postalAddress: PostalAddress
    radiusMeters: float

@typing.type_check_only
class JobProcessingOptions(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    htmlSanitization: typing_extensions.Literal[
        "HTML_SANITIZATION_UNSPECIFIED",
        "HTML_SANITIZATION_DISABLED",
        "SIMPLE_FORMATTING_ONLY",
    ]

@typing.type_check_only
class JobQuery(typing_extensions.TypedDict, total=False):
    categories: typing.List[str]
    commuteFilter: CommutePreference
    companyDisplayNames: typing.List[str]
    companyNames: typing.List[str]
    compensationFilter: CompensationFilter
    customAttributeFilter: str
    disableSpellCheck: bool
    employmentTypes: typing.List[str]
    languageCodes: typing.List[str]
    locationFilters: typing.List[LocationFilter]
    publishDateRange: typing_extensions.Literal[
        "DATE_RANGE_UNSPECIFIED",
        "PAST_24_HOURS",
        "PAST_WEEK",
        "PAST_MONTH",
        "PAST_YEAR",
        "PAST_3_DAYS",
    ]
    query: str

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListCompaniesResponse(typing_extensions.TypedDict, total=False):
    companies: typing.List[Company]
    metadata: ResponseMetadata
    nextPageToken: str

@typing.type_check_only
class ListCompanyJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    metadata: ResponseMetadata
    nextPageToken: str
    totalSize: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    metadata: ResponseMetadata
    nextPageToken: str

@typing.type_check_only
class LocationFilter(typing_extensions.TypedDict, total=False):
    distanceInMiles: float
    isTelecommute: bool
    latLng: LatLng
    name: str
    regionCode: str

@typing.type_check_only
class MatchingJob(typing_extensions.TypedDict, total=False):
    commuteInfo: CommuteInfo
    job: Job
    jobSummary: str
    jobTitleSnippet: str
    searchTextSnippet: str

@typing.type_check_only
class MendelDebugInput(typing_extensions.TypedDict, total=False):
    namespacedDebugInput: typing.Dict[str, typing.Any]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class NamespacedDebugInput(typing_extensions.TypedDict, total=False):
    absolutelyForcedExpNames: typing.List[str]
    absolutelyForcedExpTags: typing.List[str]
    absolutelyForcedExps: typing.List[int]
    conditionallyForcedExpNames: typing.List[str]
    conditionallyForcedExpTags: typing.List[str]
    conditionallyForcedExps: typing.List[int]
    disableAutomaticEnrollmentSelection: bool
    disableExpNames: typing.List[str]
    disableExpTags: typing.List[str]
    disableExps: typing.List[int]
    disableManualEnrollmentSelection: bool
    disableOrganicSelection: bool
    forcedFlags: typing.Dict[str, typing.Any]
    forcedRollouts: typing.Dict[str, typing.Any]

@typing.type_check_only
class NumericBucketingOption(typing_extensions.TypedDict, total=False):
    bucketBounds: typing.List[float]
    requiresMinMax: bool

@typing.type_check_only
class NumericBucketingResult(typing_extensions.TypedDict, total=False):
    counts: typing.List[BucketizedCount]
    maxValue: float
    minValue: float

@typing.type_check_only
class PostalAddress(typing_extensions.TypedDict, total=False):
    addressLines: typing.List[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: typing.List[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class RequestMetadata(typing_extensions.TypedDict, total=False):
    deviceInfo: DeviceInfo
    domain: str
    sessionId: str
    userId: str

@typing.type_check_only
class ResponseMetadata(typing_extensions.TypedDict, total=False):
    experimentIdList: typing.List[int]
    mode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED",
        "JOB_SEARCH",
        "FEATURED_JOB_SEARCH",
        "EMAIL_ALERT_SEARCH",
    ]
    requestId: str

@typing.type_check_only
class SearchJobsRequest(typing_extensions.TypedDict, total=False):
    disableRelevanceThresholding: bool
    enableBroadening: bool
    enablePreciseResultSize: bool
    filters: JobFilters
    histogramFacets: HistogramFacets
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED", "SMALL", "MINIMAL", "FULL"
    ]
    mode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED",
        "JOB_SEARCH",
        "FEATURED_JOB_SEARCH",
        "EMAIL_ALERT_SEARCH",
    ]
    offset: int
    orderBy: typing_extensions.Literal[
        "SORT_BY_UNSPECIFIED",
        "RELEVANCE_DESC",
        "PUBLISHED_DATE_DESC",
        "UPDATED_DATE_DESC",
        "TITLE",
        "TITLE_DESC",
        "ANNUALIZED_BASE_COMPENSATION",
        "ANNUALIZED_TOTAL_COMPENSATION",
        "ANNUALIZED_BASE_COMPENSATION_DESC",
        "ANNUALIZED_TOTAL_COMPENSATION_DESC",
    ]
    pageSize: int
    pageToken: str
    query: JobQuery
    requestMetadata: RequestMetadata
    sortBy: typing_extensions.Literal[
        "SORT_BY_UNSPECIFIED",
        "RELEVANCE_DESC",
        "PUBLISHED_DATE_DESC",
        "UPDATED_DATE_DESC",
        "TITLE",
        "TITLE_DESC",
        "ANNUALIZED_BASE_COMPENSATION",
        "ANNUALIZED_TOTAL_COMPENSATION",
        "ANNUALIZED_BASE_COMPENSATION_DESC",
        "ANNUALIZED_TOTAL_COMPENSATION_DESC",
    ]

@typing.type_check_only
class SearchJobsResponse(typing_extensions.TypedDict, total=False):
    appliedCommuteFilter: CommutePreference
    appliedJobLocationFilters: typing.List[JobLocation]
    estimatedTotalSize: str
    histogramResults: HistogramResults
    jobView: typing_extensions.Literal[
        "JOB_VIEW_UNSPECIFIED", "SMALL", "MINIMAL", "FULL"
    ]
    matchingJobs: typing.List[MatchingJob]
    metadata: ResponseMetadata
    nextPageToken: str
    numJobsFromBroadenedQuery: int
    spellResult: SpellingCorrection
    totalSize: str

@typing.type_check_only
class SpellingCorrection(typing_extensions.TypedDict, total=False):
    corrected: bool
    correctedText: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

@typing.type_check_only
class UpdateJobRequest(typing_extensions.TypedDict, total=False):
    disableStreetAddressResolution: bool
    job: Job
    processingOptions: JobProcessingOptions
    updateJobFields: str
