# APP docs

Guide to write docs.


## Endpoints

**Template:**
```md
# POST /
**Description:**

## Request

### Authentication
- Required:
- Type:

### Headers
-

### Body


## Responses
-

```

**Example:**
```md
# POST /auth/login
**Description:** Log in.

## Request

### Authentication
- Required: No

### Headers


### Body
- email (str): Unique user's email that is indexed in the database.
- password (str): Password literal string that is going to be compared against a hash.

## Responses
- 200: Returns a JWT with user data.
- 401: Incorrect password.
- 404: User's email not found.
- 412: User not verified yet.
- 422: Unprocessable entity.

```
