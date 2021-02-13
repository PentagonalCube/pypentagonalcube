"""

    A file to generate

"""
#
#   :builtins:
import os

#
#   :packages:
import typer

#
#   :statics:
TEMPLATE_SERVERLESS_FILE_PATH = "templates/serverless.yml"
TEMPLATE_FLASK_FILE_PATH = "templates/flask.py"
DEFAULT_OUTPUT_DIRECTORY = "/tmp/"
LINE_BREAK_40 = "========================================"
LINE_BREAK_60 = "============================================================"
DEFAULT_LINE_BREAK = f"{LINE_BREAK_40}{LINE_BREAK_40}"

#
#   :runtimes:
app = typer.Typer()


def cat_(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        file_data = f.read()
    message = f"\n{file_path}"
    message += f"\n{DEFAULT_LINE_BREAK}"
    message += "\n\n"
    message += file_data
    message += "\n\n"
    message += f"{DEFAULT_LINE_BREAK}\n"

    #
    #   Echo this message into the console.
    typer.echo(message)


def formatted_message(message) -> str:
    string_ = ""
    string_ += f"\npypentagonalcube - quickstart"
    string_ += f"\n============================="
    string_ += f"\n\n:message:"
    string_ += f"\n{message}"
    string_ += "\n"
    return string_


def copy_file(base_file_path: str, new_directory: str, new_file_name: str) -> str:
    new_file_path = os.path.join(new_directory, new_file_name)
    with open(base_file_path, "r", encoding="utf-8") as f:
        file_data = f.read()
    with open(new_file_path, "w", encoding="utf-8") as f:
        f.write(file_data)
    return new_file_path


@app.command()
def flask():
    #
    #   Copy the file over to the new location.
    flask_file_name = "flask.py"
    flask_file_path = copy_file(
        base_file_path=TEMPLATE_FLASK_FILE_PATH,
        new_directory=DEFAULT_OUTPUT_DIRECTORY, new_file_name=flask_file_name
    )

    typer.echo(formatted_message(
        f"ok, copied over the flask.py template to: '{flask_file_path}'"
    ))
    # cat_(file_path=flask_file_path)


@app.command()
def serverless():
    #
    #   Copy the file over to the new location.
    serverless_file_name = "serverless.yml"
    serverless_file_path = copy_file(
        base_file_path=TEMPLATE_SERVERLESS_FILE_PATH,
        new_directory=DEFAULT_OUTPUT_DIRECTORY, new_file_name=serverless_file_name
    )

    typer.echo(formatted_message(
        f"ok, copied over the serverless.yml template to: '{serverless_file_path}'"
    ))
    # cat_(file_path=serverless_file_path)


if __name__ == "__main__":
    app()
