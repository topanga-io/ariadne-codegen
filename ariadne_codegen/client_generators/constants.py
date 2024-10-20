import ast
from pathlib import Path

SIMPLE_TYPE_MAP = {
    "String": "str",
    "ID": "str",
    "Int": "int",
    "Boolean": "bool",
    "Float": "Decimal",
}

UPLOAD_CLASS_NAME = "Upload"
INPUT_SCALARS_MAP = {**SIMPLE_TYPE_MAP, "Upload": UPLOAD_CLASS_NAME}

OPTIONAL = "Optional"
LIST = "List"
UNION = "Union"
ANY = "Any"
TYPE = "Type"
TYPE_CHECKING = "TYPE_CHECKING"
DECIMAL = "Decimal"
DICT = "Dict"
TUPLE = "Tuple"
CALLABLE = "Callable"
ANNOTATED = "Annotated"
LITERAL = "Literal"
ASYNC_ITERATOR = "AsyncIterator"
DOCUMENT_NODE = "DocumentNode"
OPERATION_DEFINITION_NODE = "OperationDefinitionNode"
NAME_NODE = "NameNode"
SELECTION_SET_NODE = "SelectionSetNode"
SELECTION_NODE = "SelectionNode"
PRINT_AST = "print_ast"
OPERATION_TYPE = "OperationType"
VARIABLE_DEFINITION_NODE = "VariableDefinitionNode"
VARIABLE_NODE = "VariableNode"
NAMED_TYPE_NODE = "NamedTypeNode"

HTTPX = "httpx"
HTTPX_RESPONSE = "httpx.Response"

TIMESTAMP_COMMENT = "# Generated by ariadne-codegen on {}"
STABLE_COMMENT = "# Generated by ariadne-codegen"
SOURCE_COMMENT = "# Source: {}"
COMMENT_DATETIME_FORMAT = "%Y-%m-%d %H:%M"

BASE_OPERATION_FILE_PATH = Path(__file__).parent / "dependencies" / "base_operation.py"
BASE_GRAPHQL_OPERATION_CLASS_NAME = "BaseGraphQLOperation"
BASE_GRAPHQL_FIELD_CLASS_NAME = "GraphQLField"
CUSTOM_FIELDS_FILE_PATH = Path(__file__).parent / "custom_fields.py"
CUSTOM_FIELDS_TYPING_FILE_PATH = Path(__file__).parent / "custom_typing_fields.py"

BASE_MODEL_FILE_PATH = Path(__file__).parent / "dependencies" / "base_model.py"
BASE_MODEL_CLASS_NAME = "BaseModel"
BASE_MODEL_IMPORT = ast.ImportFrom(
    module=BASE_MODEL_FILE_PATH.stem, names=[ast.alias(BASE_MODEL_CLASS_NAME)], level=1
)
UPLOAD_IMPORT = ast.ImportFrom(
    module=BASE_MODEL_FILE_PATH.stem, names=[ast.alias(UPLOAD_CLASS_NAME)], level=1
)
UNSET_NAME = "UNSET"
UNSET_TYPE_NAME = "UnsetType"
UNSET_IMPORT = ast.ImportFrom(
    module=BASE_MODEL_FILE_PATH.stem,
    names=[ast.alias(UNSET_NAME), ast.alias(UNSET_TYPE_NAME)],
    level=1,
)

EXCEPTIONS_FILE_PATH = Path(__file__).parent / "dependencies" / "exceptions.py"

TYPENAME_FIELD_NAME = "__typename"
TYPENAME_ALIAS = "typename__"

TYPING_MODULE = "typing"
GRAPHQL_MODULE = "graphql"
DECIMAL_MODULE = "decimal"
PYDANTIC_MODULE = "pydantic"
FIELD_CLASS = "Field"
ALIAS_KEYWORD = "alias"
DEFAULT_KEYWORD = "default"
DISCRIMINATOR_KEYWORD = "discriminator"
MODEL_VALIDATE_METHOD = "model_validate"
PLAIN_SERIALIZER = "PlainSerializer"
BEFORE_VALIDATOR = "BeforeValidator"
MODEL_REBUILD_METHOD = "model_rebuild"

ENUM_MODULE = "enum"
ENUM_CLASS = "Enum"

MIXIN_NAME = "mixin"
MIXIN_FROM_NAME = "from"
MIXIN_IMPORT_NAME = "import"

SKIP_DIRECTIVE_NAME = "skip"
INCLUDE_DIRECTIVE_NAME = "include"

KWARGS_NAMES = "kwargs"

DEFAULT_ASYNC_BASE_CLIENT_PATH = (
    Path(__file__).parent / "dependencies" / "async_base_client.py"
)
DEFAULT_ASYNC_BASE_CLIENT_NAME = "AsyncBaseClient"

DEFAULT_ASYNC_BASE_CLIENT_OPEN_TELEMETRY_PATH = (
    Path(__file__).parent / "dependencies" / "async_base_client_open_telemetry.py"
)
DEFAULT_ASYNC_BASE_CLIENT_OPEN_TELEMETRY_NAME = "AsyncBaseClientOpenTelemetry"

DEFAULT_BASE_CLIENT_PATH = Path(__file__).parent / "dependencies" / "base_client.py"
DEFAULT_BASE_CLIENT_NAME = "BaseClient"

DEFAULT_BASE_CLIENT_OPEN_TELEMETRY_PATH = (
    Path(__file__).parent / "dependencies" / "base_client_open_telemetry.py"
)
DEFAULT_BASE_CLIENT_OPEN_TELEMETRY_NAME = "BaseClientOpenTelemetry"


GRAPHQL_CLIENT_EXCEPTIONS_NAMES = [
    "GraphQLClientError",
    "GraphQLClientHttpError",
    "GraphQLClientInvalidResponseError",
    "GraphQLClientGraphQLError",
    "GraphQLClientGraphQLMultiError",
]

SCALARS_PARSE_DICT_NAME = "SCALARS_PARSE_FUNCTIONS"
SCALARS_SERIALIZE_DICT_NAME = "SCALARS_SERIALIZE_FUNCTIONS"

OPERATION_TYPES = ("Query", "Mutation", "Subscription")

GRAPHQL_OBJECT_SUFFIX = "Fields"
GRAPHQL_INTERFACE_SUFFIX = "Interface"
GRAPHQL_FIELD_SUFFIX = "GraphQLField"
GRAPHQL_UNION_SUFFIX = "Union"
GRAPHQL_BASE_FIELD_CLASS = "GraphQLField"
