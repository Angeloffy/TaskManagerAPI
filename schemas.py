from marshmallow import Schema, fields, validate, ValidationError


class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class TaskSchema_update(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=False)
    description = fields.Str(required=False)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
