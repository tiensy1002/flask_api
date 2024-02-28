from flask_restx import Resource, fields, Namespace


create_admin_namespace = Namespace("create_admin", "Admin api")

create_admin_model = create_admin_namespace.model(
    "admin",
    {"message": fields.String(readonly=True, description="admin name")},
)

response = {"message": "post admin"}


@create_admin_namespace.route("")
class Admin(Resource):

    @create_admin_namespace.marshal_list_with(create_admin_model)
    @create_admin_namespace.response(500, "Internal Server error")
    def post(self):
        """Create admin"""

        return response
