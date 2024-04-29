# fastapi-project-builder
快速构建FastAPI项目结构

#### 脚本使用

1. 在命令行或终端中运行此脚本：`python gen_fastapi_project_builder.py`。
2. 根据提示输入你想要的项目名称。
3. 脚本将在当前目录下创建项目结构。



#### 目录解析

1. 将所有主要目录存放在 `src` 文件夹中
   1. `src/` - 应用的最高层级，包含通用的模型、配置和常量等。
   2. `src/main.py` - 项目的根目录，初始化 FastAPI 应用。
2. 每个包括自己的路由器、模式、模型等。
   1. `router.py` - 每个模块的核心，包含所有端点。
   2. `schemas.py` - 用于 pydantic 模型。
   3. `models.py` - 用于数据库模型。
   4. `service.py` - 模块特定的业务逻辑。
   5. `dependencies.py` - 路由器依赖。
   6. `constants.py` - 模块特定的常量和错误代码。
   7. `config.py` - 例如环境变量。
   8. `utils.py` - 非业务逻辑功能，例如响应规范化、数据丰富等。
   9. `exceptions.py` - 模块特定的异常，例如 `PostNotFound`、`InvalidUserData`。
