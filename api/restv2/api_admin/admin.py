from flask_restx import Resource, fields, Namespace


admin_namespace = Namespace("admin", "Admin api")

admin_model = admin_namespace.model(
    "admin",
    {"message": fields.String(readonly=True, description="admin")},
)

response = {"message": "get admin"}


@admin_namespace.route("/hello")
class HelloWorld(Resource):

    @admin_namespace.marshal_list_with(admin_model)
    @admin_namespace.response(500, "Internal Server error")
    def get(self):
        """admin"""

        return response
