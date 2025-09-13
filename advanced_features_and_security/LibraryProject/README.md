This creates a django app for exploration

# Django Groups & Permissions

### Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
Configured via Django Admin:
- **Editors**: can_view, can_create, can_edit
- **Viewers**: can_view
- **Admins**: all permissions

### Enforcement
Views are protected using `@permission_required` decorators
(e.g., `@permission_required('relationship_app.can_edit')`).