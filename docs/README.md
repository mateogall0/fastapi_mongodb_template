# APP docs

Guide to write docs.

**Indications:**
- Addition symbol (+) next to name for when attribute is new.
- Substraction symbol (-) next to name for when attribute is removed.

## Endpoints

**Template:**
```md
| Method | Route | Description | Version |
|:--|:--|:--|:--|
| `GET` | `/v1/example` | Example description | 1.0.0 |
```
## DB schema

**Template:**
```md
## Name

| Attribute | Type | Constraints | Description | Version |
|:--|:--|:--|:--|:--|
| `_id` | `ObjectId` | Auto-Generated, Required, Unique, Immutable | Unique ID for the document among the collection | 1.0.0 |
| `created_at` | `Timestamp` | Required, Immutable, Default(NOW) | Time of indexation of document in database | 1.0.0 |
| `updated_at` | `Timestamp` | Auto-Updated, Required, Default(NOW) | Last time the document data was updated | 1.0.0 |
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
