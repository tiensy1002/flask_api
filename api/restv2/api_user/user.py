from flask_restx import Resource, fields, Namespace


hello_namespace = Namespace("helloworld", "Hello World related endpoints")

hello_world_model = hello_namespace.model(
    "HelloWorld",
    {"message": fields.String(readonly=True, description="Hello world message")},
)

hello_world_example = {"message": "Hello World!"}


@hello_namespace.route("/hello")
class HelloWorld(Resource):

    @hello_namespace.marshal_list_with(hello_world_model)
    @hello_namespace.response(500, "Internal Server error")
    def get(self):
        """Hello world message endpoint"""

        return hello_world_example
