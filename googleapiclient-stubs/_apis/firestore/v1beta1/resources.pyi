import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class FirestoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatabasesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    database: str,
                    body: BatchGetDocumentsRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchGetDocumentsResponseHttpRequest: ...
                def batchWrite(
                    self,
                    *,
                    database: str,
                    body: BatchWriteRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchWriteResponseHttpRequest: ...
                def beginTransaction(
                    self,
                    *,
                    database: str,
                    body: BeginTransactionRequest = ...,
                    **kwargs: typing.Any
                ) -> BeginTransactionResponseHttpRequest: ...
                def commit(
                    self,
                    *,
                    database: str,
                    body: CommitRequest = ...,
                    **kwargs: typing.Any
                ) -> CommitResponseHttpRequest: ...
                def createDocument(
                    self,
                    *,
                    parent: str,
                    collectionId: str,
                    body: Document = ...,
                    documentId: str = ...,
                    mask_fieldPaths: typing.Union[str, typing.List[str]] = ...,
                    **kwargs: typing.Any
                ) -> DocumentHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    currentDocument_exists: bool = ...,
                    currentDocument_updateTime: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    mask_fieldPaths: typing.Union[str, typing.List[str]] = ...,
                    readTime: str = ...,
                    transaction: str = ...,
                    **kwargs: typing.Any
                ) -> DocumentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    collectionId: str,
                    mask_fieldPaths: typing.Union[str, typing.List[str]] = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    showMissing: bool = ...,
                    transaction: str = ...,
                    **kwargs: typing.Any
                ) -> ListDocumentsResponseHttpRequest: ...
                def listCollectionIds(
                    self,
                    *,
                    parent: str,
                    body: ListCollectionIdsRequest = ...,
                    **kwargs: typing.Any
                ) -> ListCollectionIdsResponseHttpRequest: ...
                def listen(
                    self,
                    *,
                    database: str,
                    body: ListenRequest = ...,
                    **kwargs: typing.Any
                ) -> ListenResponseHttpRequest: ...
                def partitionQuery(
                    self,
                    *,
                    parent: str,
                    body: PartitionQueryRequest = ...,
                    **kwargs: typing.Any
                ) -> PartitionQueryResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Document = ...,
                    currentDocument_exists: bool = ...,
                    currentDocument_updateTime: str = ...,
                    mask_fieldPaths: typing.Union[str, typing.List[str]] = ...,
                    updateMask_fieldPaths: typing.Union[str, typing.List[str]] = ...,
                    **kwargs: typing.Any
                ) -> DocumentHttpRequest: ...
                def rollback(
                    self,
                    *,
                    database: str,
                    body: RollbackRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def runQuery(
                    self,
                    *,
                    parent: str,
                    body: RunQueryRequest = ...,
                    **kwargs: typing.Any
                ) -> RunQueryResponseHttpRequest: ...
                def write(
                    self,
                    *,
                    database: str,
                    body: WriteRequest = ...,
                    **kwargs: typing.Any
                ) -> WriteResponseHttpRequest: ...
            @typing.type_check_only
            class IndexesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirestoreAdminV1beta1Index = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1beta1IndexHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirestoreAdminV1beta1ListIndexesResponseHttpRequest: ...
            def exportDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1beta1ExportDocumentsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def importDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1beta1ImportDocumentsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def documents(self) -> DocumentsResource: ...
            def indexes(self) -> IndexesResource: ...
        def databases(self) -> DatabasesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BatchGetDocumentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchGetDocumentsResponse: ...

@typing.type_check_only
class BatchWriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchWriteResponse: ...

@typing.type_check_only
class BeginTransactionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BeginTransactionResponse: ...

@typing.type_check_only
class CommitResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CommitResponse: ...

@typing.type_check_only
class DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Document: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirestoreAdminV1beta1Index: ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirestoreAdminV1beta1ListIndexesResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class ListCollectionIdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCollectionIdsResponse: ...

@typing.type_check_only
class ListDocumentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDocumentsResponse: ...

@typing.type_check_only
class ListenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListenResponse: ...

@typing.type_check_only
class PartitionQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PartitionQueryResponse: ...

@typing.type_check_only
class RunQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RunQueryResponse: ...

@typing.type_check_only
class WriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> WriteResponse: ...
