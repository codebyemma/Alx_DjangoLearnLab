# Django Permissions & Groups Setup

## Custom Permissions
The Article model includes custom permissions:
- can_view
- can_create
- can_edit
- can_delete

These permissions control what actions a user can perform on articles.

## Groups Created
1. Viewers:
   - can_view

2. Editors:
   - can_view
   - can_create
   - can_edit

3. Admins:
   - can_view
   - can_create
   - can_edit
   - can_delete

## How It Works in Views
Django's permission_required decorator is used:
@permission_required('yourapp.can_edit', raise_exception=True)

This ensures that only users with the correct permissions may access protected views.

## Testing
- Create sample users in Django Admin.
- Assign each user to one of the defined groups.
- Log in as each user and test allowed/blocked actions.
