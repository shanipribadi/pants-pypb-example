protobuf_sources(
    dependencies=[
        ]
    )

python_distribution(
    name="dist",
    dependencies=[
        ":package",
        "//:root#googleapis-common-protos",
        "!!//src/protos/google/type:type",
    ],
    provides=python_artifact(
        name="my-package-proto",
        version="0.0.1",
    ),
)
