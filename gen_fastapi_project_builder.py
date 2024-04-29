import os

# 定义文件和文件夹结构
def create_project_structure(project_name):
    project_structure = {
        f"{project_name}/": [
            "alembic/",
            "src/",
            "tests/",
            "templates/index.html",
            "requirements/base.txt",
            "requirements/dev.txt",
            "requirements/prod.txt",
            ".env",
            ".gitignore",
            "logging.ini",
            "alembic.ini",
            "src/auth/router.py",
            "src/auth/schemas.py",
            "src/auth/models.py",
            "src/auth/dependencies.py",
            "src/auth/config.py",
            "src/auth/constants.py",
            "src/auth/exceptions.py",
            "src/auth/service.py",
            "src/auth/utils.py",
            "src/aws/client.py",
            "src/aws/schemas.py",
            "src/aws/config.py",
            "src/aws/constants.py",
            "src/aws/exceptions.py",
            "src/aws/utils.py",
            "src/posts/router.py",
            "src/posts/schemas.py",
            "src/posts/models.py",
            "src/posts/dependencies.py",
            "src/posts/constants.py",
            "src/posts/exceptions.py",
            "src/posts/service.py",
            "src/posts/utils.py",
            "src/config.py",
            "src/models.py",
            "src/exceptions.py",
            "src/pagination.py",
            "src/database.py",
            "src/main.py",
            "tests/auth/",
            "tests/aws/",
            "tests/posts/"
        ]
    }

    for path in project_structure[project_name + "/"]:
        if path.endswith("/"):
            os.makedirs(os.path.join(project_name, path), exist_ok=True)
        else:
            # Ensure the directory exists before creating a file
            os.makedirs(os.path.dirname(os.path.join(project_name, path)), exist_ok=True)
            with open(os.path.join(project_name, path), 'w') as f:
                pass  # You can pre-populate files here if necessary

# 主程序入口
if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    create_project_structure(project_name)
    print(f"Project '{project_name}' has been created with the specified structure.")
