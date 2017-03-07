import cx_Freeze
executables =[cx_Freeze.Executable("snake.py")]
cx_Freeze.setup(
    name="block",
    options={"build_exe":{"packages":["pygame"]}},

    description ="Block Game",
    executables = executables

    )

              
