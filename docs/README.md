# APP docs

Guide to write docs.

## Endpoints

**Template:**
```md
# v
**Description:**

## POST /
**Description:**

### Request

##### Authentication
- Required:
- Type:

##### Headers
-

##### Body


### Responses
-

```

**Example:**
```md
# v1.1.0
**Description:** Add new endpoint for log in.

## POST /auth/login
**Description:** Log in.

### Request

##### Authentication
- Required: No

##### Headers


##### Body
- email (str): Unique user's email that is indexed in the database.
- password (str): Password literal string that is going to be compared against a hash.

### Responses
- 200: Returns a JWT with user data.
- 401: Incorrect password.
- 404: User's email not found.
- 412: User not verified yet.
- 422: Unprocessable entity.

```

## DB schema

**Template:**


```md
# v

## Name

| Column Name | Data Type | Constraints | Description |
|:--|:--|:--|:--|
| _id | ObjectId | Auto-Generated, Required, Unique, Immutable | Unique ID for the document among the collection |
| created_at | Timestamp | Required, Immutable, Default(NOW) | Time of indexation of document in database |
| updated_at | Timestamp | Auto-Updated, Required, Default(NOW) | Last time the document data was updated |
```

**BSON data types:**
- Double
- String
- Object
- Array
- BinData
- ObjectId
- Boolean
- Date
- NULL
- Regex
- JS
- Int32
- Timestamp
- Int64
- Decimal28
- MinKey
- MaxKey

**Constraints:**
- Required
- Min()
- Max()
- MinLength()
- MaxLength()
- Pattern()
- Enum()
- Unique
- Immutable
- Auto-Generated
- Auto-Updated
- Default()
- OneOf()
- AllOf()
- AnyOf()
- Not()
- UniqueItems()
- Const
- Dependencies()










