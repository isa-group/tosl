## SHACL Validator Test Cases

### ✅ Valid

| File                 | Description                                             |
|----------------------|---------------------------------------------------------|
| permission_complete.ttl     | Contains required description, action, assignee, target |

### ❌ Invalid

| File                 | Description                                |
|----------------------|--------------------------------------------|
| permission_without_action.ttl     | Missing `odrl:action`                      |
