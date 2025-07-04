# APP docs

Guide to write docs.

**Indications:**
- Addition symbol (+) next to name for when attribute is new.
- Substraction symbol (-) next to name for when attribute is removed.

## Endpoints

**Template:**
| Method | Route | Description | Version |
|:--|:--|:--|:--|
| `GET` | `/v1/example` | Example description | 1.0.0 |

## DB schema

**Template:**


```md
# v

## Name

| Attribute Name | Data Type | Constraints | Description |
|:--|:--|:--|:--|
| +_id | ObjectId | Auto-Generated, Required, Unique, Immutable | Unique ID for the document among the collection |
| +created_at | Timestamp | Required, Immutable, Default(NOW) | Time of indexation of document in database |
| +updated_at | Timestamp | Auto-Updated, Required, Default(NOW) | Last time the document data was updated |
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
