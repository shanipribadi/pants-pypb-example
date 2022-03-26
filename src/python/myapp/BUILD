pex_binary(
    name="app",
    entry_point="app.py",
    dependencies=[
        "!!src/protos/google/type:type",
    ]
)

python_sources(
    dependencies=[
        "//:root#googleapis-common-protos",
    ]
)

python_distribution(
    name="dist",
    dependencies=[
        ":myapp",
        "!!src/protos/google/type:type",
    ],
    provides=python_artifact(
        name="my-app",
        version="0.0.1",
    ),
)
